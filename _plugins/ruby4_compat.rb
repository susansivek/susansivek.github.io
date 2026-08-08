# Local-only: github-pages ships Liquid 4.0.3, which calls Object#tainted?
# (removed in Ruby 3.2+). GitHub Pages ignores custom plugins.
module Liquid
  class Variable
    def taint_check(_obj)
      # no-op
    end
  end
end
