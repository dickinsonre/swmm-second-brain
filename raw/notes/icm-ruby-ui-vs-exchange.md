# The same ICM Ruby query starts differently in GeoPlan and Exchange

**Status:** seed
**Date:** 2026-11-16

## The idea

Use the same node count to check both scripting environments. In the ICM desktop UI, `WSApplication.current_network` returns the network in the focused GeoPlan. In Exchange, give the script the database and the network's scripting path. Autodesk documents ICM Exchange for Ultimate licenses.

## Proof / from scratch

Pick a small InfoWorks network. Open its base scenario in GeoPlan and count its nodes with this UI script.

```ruby
raise 'Run this script in the ICM UI.' unless WSApplication.ui?

network = WSApplication.current_network
raise 'Open the test network in GeoPlan.' unless network

puts network.row_objects('hw_node').length
```

Use a saved copy of that network for the Exchange example. Save the following as `count-nodes.rb`. The script reads model data and prints a count. The `false` argument to `WSApplication.open` skips the database upgrade.

```ruby
raise 'Run this script in ICM Exchange.' if WSApplication.ui?

database_path, network_path, table = ARGV
unless database_path && network_path && %w[hw_node sw_node].include?(table)
  abort 'Pass the database path, network scripting path, and node table.'
end

database = WSApplication.open(database_path, false)
model = database.model_object(network_path)
abort 'Could not find the network at the supplied scripting path.' unless model

network = model.open
puts network.row_objects(table).length
```

From PowerShell in the installed ICM directory, substitute the real script path, database path, and network scripting path. The optional `-login` flag starts sign-in if needed.

```powershell
.\ICMExchange.exe 'C:\Models\count-nodes.rb' -login 'C:\Models\Test.icmm' '<network scripting path>' hw_node
```

Both scripts should return the same count for the same saved base network. Repeat with `sw_node` for an ICM SWMM test network. The examples are based on the documented API and await a run in ICM.

## Links

- [Autodesk ICM Exchange command line](https://help.autodesk.com/view/IWICMS/2027/ENU/?guid=GUID-249316C9-AEFD-43E0-ABB6-F1D55E4DB25F)
- [Autodesk WSApplication reference](https://help.autodesk.com/view/IWICMS/2027/ENU/?guid=Innovyze_Exchange_Classes_ICM_wsapplication_html)
- [Autodesk WSDatabase reference](https://help.autodesk.com/view/IWICMS/2027/ENU/?guid=Innovyze_Exchange_Classes_ICM_wsdatabase_html)
- [ICM Ruby version compatibility](./icm-ruby-version-compatibility.md)
