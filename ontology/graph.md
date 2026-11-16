# Ontology graph (built)

Built by `tools/ontology.py` from the Relations tables; do not edit by hand. Classes from `is_a` are shown in italics inside each box; a relation with a `verification` qualifier shows it in parentheses (run, pending or documented). See [ONTOLOGY.md](../ONTOLOGY.md).

## wiki/concepts/icm-2d-rainfall-and-infiltration.md

```mermaid
flowchart LR
  n0["icm-iw:Fixed2D<br/><i>Infiltration method</i>"]
  n1["icm-iw:InfiltrationSurface2D"]
  n2["icm-iw:Horton2D<br/><i>Infiltration method</i>"]
  n3["icm-iw:ConstInf2D<br/><i>Infiltration method</i>"]
  n4["icm-iw:GreenAmpt2D<br/><i>Infiltration method</i>"]
  n5["icm-iw:DefConLoss2D<br/><i>Infiltration method</i>"]
  n6["icm-iw:CNSWMM2D<br/><i>Infiltration method</i>"]
  n7["icm:2025.1<br/><i>Release</i>"]
  n8["icm:ICM"]
  n9["icm-iw:InitialAbstractionFactor<br/><i>Parameter</i>"]
  n10["icm-iw:CurveNumber<br/><i>Parameter</i>"]
  n11["icm-iw:DryingTime<br/><i>Parameter</i>"]
  n12["icm-iw:CNSWMMAntecedentMoistureCondition<br/><i>Parameter</i>"]
  n13["icm-iw:InitialConditions2D"]
  n14["icm-iw:SubcatchmentCN<br/><i>Infiltration method</i>"]
  n15["icm-iw:OutsideSubcatchments<br/><i>Setting</i>"]
  n16["icm-iw:Zone2D"]
  n0 -->|"part of"| n1
  n2 -->|"part of"| n1
  n3 -->|"part of"| n1
  n4 -->|"part of"| n1
  n5 -->|"part of"| n1
  n6 -->|"part of"| n1
  n6 -->|"available in (documented)"| n7
  n7 -->|"part of"| n8
  n6 -->|"has parameter (documented)"| n9
  n6 -->|"has parameter (documented)"| n10
  n6 -->|"has parameter (documented)"| n11
  n12 -->|"part of"| n13
  n2 -->|"approximates (run)"| n14
  n4 -->|"approximates (run)"| n14
  n3 -->|"approximates (run)"| n14
  n15 -->|"part of"| n16
```

## wiki/concepts/icm-ruby-ui-and-exchange.md

```mermaid
flowchart LR
  n0["ruby:3.4.6<br/><i>Ruby runtime</i>"]
  n1["icm:2027.0<br/><i>Release</i>"]
  n2["ruby:2.4.0<br/><i>Ruby runtime</i>"]
  n3["icm:ICM"]
  n4["icm:ICMExchange<br/><i>Program</i>"]
  n5["icm:UltimateLicense<br/><i>License</i>"]
  n6["icm:WSApplication.current_network<br/><i>Api method</i>"]
  n7["icm:UIScripting"]
  n8["icm:WSApplication.open<br/><i>Api method</i>"]
  n9["icm:WSApplication.connect_local_agent<br/><i>Api method</i>"]
  n10["icm:WSApplication.launch_sims<br/><i>Api method</i>"]
  n11["icm:WSApplication.wait_for_jobs<br/><i>Api method</i>"]
  n12["icm:JobTimeout<br/><i>Parameter</i>"]
  n0 -->|"available in (documented)"| n1
  n0 -->|"replaces (documented)"| n2
  n1 -->|"part of"| n3
  n4 -->|"part of"| n3
  n4 -->|"requires (documented)"| n5
  n6 -->|"part of"| n7
  n8 -->|"part of"| n4
  n9 -->|"part of"| n4
  n10 -->|"part of"| n4
  n11 -->|"part of"| n4
  n11 -->|"has parameter (documented)"| n12
```

## wiki/concepts/icm-tables-and-result-fields.md

```mermaid
flowchart LR
  n0["icm:InfoWorksNetwork<br/><i>Network type</i>"]
  n1["icm:ICM"]
  n2["icm:SWMMNetwork<br/><i>Network type</i>"]
  n3["icm-iw:hw_node<br/><i>Data table</i>"]
  n4["icm-iw:hw_conduit<br/><i>Data table</i>"]
  n5["icm-iw:hw_subcatchment<br/><i>Data table</i>"]
  n6["icm-swmm:sw_node<br/><i>Data table</i>"]
  n7["icm-swmm:sw_conduit<br/><i>Data table</i>"]
  n8["icm-swmm:sw_subcatchment<br/><i>Data table</i>"]
  n9["icm-iw:hw_2d_infil_surface<br/><i>Data table</i>"]
  n10["icm-iw:InfiltrationSurface2D"]
  n11["icm-iw:DEPNOD<br/><i>Result field</i>"]
  n12["icm-swmm:HEAD<br/><i>Result field</i>"]
  n13["icm-swmm:DEPTH<br/><i>Result field</i>"]
  n14["qty:WaterLevel<br/><i>Quantity</i>"]
  n15["qty:DepthAboveInlet<br/><i>Quantity</i>"]
  n16["qty:InletElevation<br/><i>Quantity</i>"]
  n0 -->|"part of"| n1
  n2 -->|"part of"| n1
  n3 -->|"part of"| n0
  n4 -->|"part of"| n0
  n5 -->|"part of"| n0
  n6 -->|"part of"| n2
  n7 -->|"part of"| n2
  n8 -->|"part of"| n2
  n3 -->|"close match (documented)"| n6
  n4 -->|"close match (documented)"| n7
  n5 -->|"close match (documented)"| n8
  n9 -->|"part of"| n0
  n10 -->|"stored in"| n9
  n11 -->|"part of"| n0
  n12 -->|"part of"| n2
  n13 -->|"part of"| n2
  n11 -->|"reports (documented)"| n14
  n12 -->|"reports (documented)"| n14
  n13 -->|"reports (documented)"| n15
  n11 -->|"close match (pending)"| n12
  n15 -->|"derived from"| n14
  n15 -->|"derived from"| n16
```
