# An ICM Ruby script needs a test in the embedded runtime

**Status:** seed
**Date:** 2026-11-16

## The idea

Autodesk documents Ruby 3.4.6 for embedded UI and Exchange scripting beginning with ICM 2027.0. Its upgrade article identifies Ruby 2.4.0 as the earlier runtime and describes `LoadError` when a script requires a library that changed or is unavailable. Keep the ICM build and Ruby version next to each script's test result.

## Proof / from scratch

Run the smoke test through the environment the script actually uses. The first line prints the ICM build, Ruby version, and whether the script is running in the UI. Test the actual `require` statements from the script before testing its model operations.

```ruby
puts "ICM #{WSApplication.version}, Ruby #{RUBY_VERSION}, UI #{WSApplication.ui?}"
require 'csv'
puts CSV.generate_line(%w[node_id level])
```

The script should print a version line followed by the CSV header `node_id,level`. For the next check, read one known node from a saved test network. Save the exact error message and library name if a dependency fails.

| Script and commit | ICM build | Ruby version | UI or Exchange | Network type | Dependencies load | Known object read |
|---|---|---|---|---|---|---|
| Your first test | | | | | | |

Start with a script you use often, such as a CSV exporter. This compatibility check awaits a run in each target ICM release.

## Links

- [Autodesk support on Ruby UI and Exchange scripts after upgrading](https://www.autodesk.com/support/technical/article/caas/sfdcarticles/sfdcarticles/Ruby-UI-and-Exchange-scripts-fail-after-upgrading-to-InfoWorks-ICM-2027-0-or-later.html)
- [Autodesk Ruby Script help](https://help.autodesk.com/cloudhelp/2027/ENU/ICM-Help/files/GUID-57F599CF-9FDE-405D-8C78-030694266390.htm)
- [UI and Exchange node count](./icm-ruby-ui-vs-exchange.md)
