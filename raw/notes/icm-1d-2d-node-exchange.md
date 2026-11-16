# The ICM node flood type sets the 1D–2D exchange relation

**Status:** seed
**Date:** 2026-11-16

## The idea

At an InfoWorks manhole, the flood type determines how water exchanges with the receiving mesh element. Record the physical opening, node ground or crest elevation, element elevation, and documented depth or elevation linkage basis. Those details give meaning to a plotted exchange flow.

## Proof / from scratch

| InfoWorks manhole flood type | Documented exchange relation |
|---|---|
| 2D | Weir relation using the node ground level for the crest and the shaft circumference for its length |
| Gully 2D | User-specified head–discharge relationship |
| Inlet 2D | User-specified inlet parameters |

Autodesk lists Outfall 2D and Connect 2D as additional node types. Check their own connection rules when locating a 2D outfall or the end of a supported 2D conduit.

Use one manhole and one small receiving depression. Drive the sewer head above the opening, then lower it while the surface retains water. Plot water levels on both sides with exchange flow on the same time axis. Confirm the crest, receiving element, sign, and timing. A useful second run raises the manhole cover above the surrounding terrain and tests the documented elevation linkage setting.

If the log reports warning 1053, identify the nodes with limited exchange and inspect the adjacent element and the plotted heads. Record the warning and the limited flow series with the run.

## Links

- [Autodesk defining 2D nodes](https://help.autodesk.com/cloudhelp/2027/ENU/ICM-Help/files/GUID-3215A6B1-1F8F-430E-956F-0AE35951D7E0.htm)
- [Autodesk support on warning 1053](https://www.autodesk.com/support/technical/article/caas/sfdcarticles/sfdcarticles/Warning-message-1053-one-or-more-nodes-had-their-flow-limited-from-the-2D-zone-in-InfoWorks-ICM.html)
- [2D benchmark cases](./icm-2d-benchmark-cases.md)
- [2D volume balance](./icm-2d-volume-balance.md)
