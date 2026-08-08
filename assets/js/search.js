(function () {
  "use strict";

  var CATEGORY_LABELS = {
    "data-science": "Data Science and Tech",
    features: "Features",
    profiles: "Profiles",
    academic: "Academic Life",
    media: "Media Industry",
  };

  var index = null;
  var loadPromise = null;

  function escapeHtml(str) {
    return String(str)
      .replace(/&/g, "&amp;")
      .replace(/</g, "&lt;")
      .replace(/>/g, "&gt;")
      .replace(/"/g, "&quot;");
  }

  function tokenize(query) {
    return query
      .toLowerCase()
      .trim()
      .split(/\s+/)
      .filter(function (t) {
        return t.length > 0;
      });
  }

  function getIndexUrl() {
    var form = document.querySelector(".site-search");
    if (form && form.getAttribute("data-index-url")) {
      return form.getAttribute("data-index-url");
    }
    var page = document.getElementById("search-page-results");
    if (page && page.getAttribute("data-index-url")) {
      return page.getAttribute("data-index-url");
    }
    return "/search.json";
  }

  function getSearchPageUrl() {
    var form = document.querySelector(".site-search");
    if (form && form.getAttribute("data-search-url")) {
      return form.getAttribute("data-search-url");
    }
    return "/search/";
  }

  function loadIndex() {
    if (index) return Promise.resolve(index);
    if (loadPromise) return loadPromise;

    var indexUrl = getIndexUrl();
    loadPromise = fetch(indexUrl)
      .then(function (response) {
        if (!response.ok) {
          throw new Error("Could not load search index (" + response.status + ")");
        }
        return response.json();
      })
      .then(function (data) {
        if (!Array.isArray(data)) {
          throw new Error("Search index is not an array");
        }
        index = data.map(function (item) {
          var cats = Array.isArray(item.categories) ? item.categories : [];
          var haystack = [
            item.title || "",
            item.excerpt || "",
            item.publication || "",
            cats.join(" "),
            cats
              .map(function (c) {
                return CATEGORY_LABELS[c] || c;
              })
              .join(" "),
          ]
            .join(" ")
            .toLowerCase();

          return {
            title: item.title || "Untitled",
            url: item.url || "#",
            date: item.date,
            publication: item.publication || "",
            excerpt: item.excerpt || "",
            haystack: haystack,
          };
        });
        return index;
      })
      .catch(function (err) {
        console.error(err);
        loadPromise = null;
        index = [];
        return index;
      });

    return loadPromise;
  }

  function scoreItem(item, tokens) {
    var title = (item.title || "").toLowerCase();
    var score = 0;

    for (var i = 0; i < tokens.length; i++) {
      var token = tokens[i];
      if (item.haystack.indexOf(token) === -1) return -1;
      if (title.indexOf(token) !== -1) score += 10;
      else score += 1;
      if (title.indexOf(token) === 0) score += 5;
    }

    return score;
  }

  function search(query, limit) {
    var tokens = tokenize(query);
    if (tokens.length === 0) {
      return Promise.resolve([]);
    }

    return loadIndex().then(function (items) {
      var ranked = items
        .map(function (item) {
          return { item: item, score: scoreItem(item, tokens) };
        })
        .filter(function (row) {
          return row.score >= 0;
        })
        .sort(function (a, b) {
          return b.score - a.score;
        });

      if (typeof limit === "number") {
        ranked = ranked.slice(0, limit);
      }

      return ranked.map(function (row) {
        return row.item;
      });
    });
  }

  function metaLine(item) {
    var meta = [];
    if (item.date) meta.push(escapeHtml(item.date));
    else meta.push("Undated");
    if (item.publication) meta.push(escapeHtml(item.publication));
    return meta.join(" · ");
  }

  function resultsUrl(query) {
    var base = getSearchPageUrl();
    return base + (base.indexOf("?") === -1 ? "?" : "&") + "q=" + encodeURIComponent(query);
  }

  /* ---- Header autocomplete ---- */

  function initAutocomplete() {
    var input = document.getElementById("site-search-input");
    var resultsEl = document.getElementById("site-search-results");
    var statusEl = document.getElementById("site-search-status");
    var form = document.querySelector(".site-search");

    if (!input || !resultsEl || !form) return;

    var debounceTimer = null;
    var activeIndex = -1;
    var previewLimit = 6;

    function setStatus(message) {
      if (statusEl) statusEl.textContent = message;
    }

    function hideResults() {
      resultsEl.hidden = true;
      resultsEl.innerHTML = "";
      activeIndex = -1;
      input.removeAttribute("aria-activedescendant");
      input.setAttribute("aria-expanded", "false");
      setStatus("");
    }

    function renderPreview(items, query, totalHint) {
      activeIndex = -1;
      input.removeAttribute("aria-activedescendant");

      if (!query.trim()) {
        hideResults();
        return;
      }

      if (items.length === 0) {
        resultsEl.innerHTML =
          '<p class="site-search-empty">No matches for “' +
          escapeHtml(query.trim()) +
          '”.</p>';
        resultsEl.hidden = false;
        input.setAttribute("aria-expanded", "true");
        setStatus("No matches");
        return;
      }

      var html = items
        .map(function (item, i) {
          return (
            '<a class="site-search-result" role="option" id="site-search-option-' +
            i +
            '" href="' +
            escapeHtml(item.url) +
            '" data-index="' +
            i +
            '">' +
            '<span class="site-search-result-title">' +
            escapeHtml(item.title) +
            "</span>" +
            '<span class="site-search-result-meta">' +
            metaLine(item) +
            "</span>" +
            "</a>"
          );
        })
        .join("");

      html +=
        '<a class="site-search-more" role="option" id="site-search-option-more" href="' +
        escapeHtml(resultsUrl(query.trim())) +
        '" data-index="more">See all results for “' +
        escapeHtml(query.trim()) +
        '”</a>';

      resultsEl.innerHTML = html;
      resultsEl.hidden = false;
      input.setAttribute("aria-expanded", "true");
      setStatus(
        items.length +
          " suggestion" +
          (items.length === 1 ? "" : "s") +
          (totalHint ? "" : "")
      );
    }

    function updateActiveOption(nextIndex) {
      var options = resultsEl.querySelectorAll("[role='option']");
      if (!options.length) return;

      if (activeIndex >= 0 && options[activeIndex]) {
        options[activeIndex].classList.remove("is-active");
      }

      activeIndex = nextIndex;
      if (activeIndex < 0) activeIndex = options.length - 1;
      if (activeIndex >= options.length) activeIndex = 0;

      options[activeIndex].classList.add("is-active");
      input.setAttribute("aria-activedescendant", options[activeIndex].id);
      options[activeIndex].scrollIntoView({ block: "nearest" });
    }

    function goToResultsPage() {
      var query = input.value.trim();
      if (!query) return;
      window.location.href = resultsUrl(query);
    }

    function runPreview() {
      var query = input.value;
      if (!query.trim()) {
        hideResults();
        return;
      }

      search(query, previewLimit)
        .then(function (items) {
          if (input.value !== query) return;
          renderPreview(items, query);
        })
        .catch(function (err) {
          console.error(err);
          resultsEl.innerHTML =
            '<p class="site-search-empty">Search isn’t available right now.</p>';
          resultsEl.hidden = false;
          setStatus("Search unavailable");
        });
    }

    input.setAttribute("aria-autocomplete", "list");
    input.setAttribute("aria-controls", "site-search-results");
    input.setAttribute("aria-expanded", "false");

    input.addEventListener("focus", function () {
      loadIndex();
      if (input.value.trim()) runPreview();
    });

    input.addEventListener("input", function () {
      window.clearTimeout(debounceTimer);
      debounceTimer = window.setTimeout(runPreview, 140);
    });

    input.addEventListener("keydown", function (event) {
      var options = resultsEl.querySelectorAll("[role='option']");

      if (event.key === "Escape") {
        if (!resultsEl.hidden) {
          hideResults();
          event.preventDefault();
        } else if (input.value) {
          input.value = "";
          hideResults();
          event.preventDefault();
        }
        return;
      }

      if (event.key === "Enter") {
        if (!resultsEl.hidden && activeIndex >= 0 && options[activeIndex]) {
          event.preventDefault();
          window.location.href = options[activeIndex].href;
          return;
        }
        event.preventDefault();
        goToResultsPage();
        return;
      }

      if (resultsEl.hidden || !options.length) return;

      if (event.key === "ArrowDown") {
        event.preventDefault();
        updateActiveOption(activeIndex + 1);
      } else if (event.key === "ArrowUp") {
        event.preventDefault();
        updateActiveOption(activeIndex - 1);
      }
    });

    form.addEventListener("submit", function (event) {
      event.preventDefault();
      var options = resultsEl.querySelectorAll("[role='option']");
      if (!resultsEl.hidden && activeIndex >= 0 && options[activeIndex]) {
        window.location.href = options[activeIndex].href;
        return;
      }
      goToResultsPage();
    });

    document.addEventListener("click", function (event) {
      if (!form.contains(event.target)) {
        hideResults();
      }
    });
  }

  /* ---- Full results page ---- */

  function initSearchPage() {
    var resultsEl = document.getElementById("search-page-results");
    var summaryEl = document.getElementById("search-page-summary");
    var input = document.getElementById("site-search-input");
    if (!resultsEl) return;

    var params = new URLSearchParams(window.location.search);
    var query = (params.get("q") || "").trim();

    if (input && query) {
      input.value = query;
    }

    if (!query) {
      if (summaryEl) {
        summaryEl.textContent =
          "Type a query in the search box above, then press Enter.";
      }
      resultsEl.innerHTML = "";
      return;
    }

    if (summaryEl) summaryEl.textContent = "Searching…";

    search(query)
      .then(function (items) {
        if (summaryEl) {
          if (items.length === 0) {
            summaryEl.textContent =
              "No matches for “" + query + "”.";
          } else {
            summaryEl.textContent =
              items.length +
              " result" +
              (items.length === 1 ? "" : "s") +
              " for “" +
              query +
              "”.";
          }
        }

        if (items.length === 0) {
          resultsEl.innerHTML =
            '<p class="empty-state">Try a shorter phrase, a title keyword, or a publication name.</p>';
          return;
        }

        resultsEl.innerHTML =
          '<ul class="post-list">' +
          items
            .map(function (item) {
              var excerpt = item.excerpt
                ? '<p class="post-item-excerpt">' +
                  escapeHtml(item.excerpt) +
                  "</p>"
                : "";
              return (
                '<li class="post-item">' +
                '<div class="post-item-meta">' +
                '<span class="post-date">' +
                (item.date ? escapeHtml(item.date) : "Undated") +
                "</span>" +
                (item.publication
                  ? '<span class="post-publication">' +
                    escapeHtml(item.publication) +
                    "</span>"
                  : "") +
                "</div>" +
                '<div class="post-item-body">' +
                '<a class="post-item-title" href="' +
                escapeHtml(item.url) +
                '">' +
                escapeHtml(item.title) +
                "</a>" +
                excerpt +
                "</div>" +
                "</li>"
              );
            })
            .join("") +
          "</ul>";
      })
      .catch(function (err) {
        console.error(err);
        if (summaryEl) {
          summaryEl.textContent = "Search isn’t available right now.";
        }
        resultsEl.innerHTML =
          '<p class="empty-state">Please try again in a moment.</p>';
      });
  }

  initAutocomplete();
  initSearchPage();
})();
