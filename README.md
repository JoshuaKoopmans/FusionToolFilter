# FusionToolFilter
Filtering of Fusion Detection Tool Results using Spanning- &amp; Junction Read Counts.




### Usage:
`filter_fusion_out.py [-h] -i INPUT -o OUTPUT`<br> 
                           &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`-t {starfusion,fusioncatcher,jaffa,arriba}`<br>
                            &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`[--threshold-junction THRESHOLD_JUNCTION]`<br>
                            &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`[--threshold-spanning THRESHOLD_SPANNING]`<br>
                            &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`[--threshold-confidence {HighConfidence,MediumConfidence,LowConfidence}]`<br>
                            &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`[--fusion-inspector {yes,no}]`

Filter output of either STAR-Fusion or fusionCatcher fusion gene detection
tool.  

Arguments:<br>
  &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`-h`, `--help`            show this help message and exit<br>
  &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`-i`, `--input`
                        Input file<br>
  &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`-o`, `--output` 
                        Desired output file name<br>
  &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`-t`, `--tool` {starfusion,fusioncatcher,jaffa,arriba}
                        Select tool that generated output file<br>
  &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`--threshold-junction` 
                        Amount of junction reads to filter by (only starfusion
                        & arriba)<br>
  &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`--threshold-spanning` 
                        Amount of spanning frag reads to filter by (only
                        starfusion & arriba)<br>
  &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`--threshold-confidence` {HighConfidence,MediumConfidence,LowConfidence}
                        Confidence level to filter by (only jaffa)<br>
  &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`--fusion-inspector` {yes,no}
                        Additional filtered file with the first column
                        formatted for FusionInspector




---

Directory | Content
--------- | -------
modules   | Fusion Detection Tool methods
tests     | Unittests
