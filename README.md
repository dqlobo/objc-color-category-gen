# objc-color-category-gen
Python script that generates a category class of UIColor in Objective C. Works great with XML exported files from paletton.com. See Format for details.
# Usage
*Requires Python 3*
SKU is the 
```
> python3 color_from_xml.py -i<inputfile> -s<SKU>
```

# Format
This script just traverses and XML file and extracts properties that correspond to color name and rgb (as floats). The format is as follows:
```
<RootNode>
  <ColorGroup1>
    <Color id="crimson" r0="0.7" b0="0.2" g0="0.2" />
    <Color id="lighterCrimson" r0="1" b0="0.2" g0="0.2" />
  </ColorGroup1>
  <ColorGroup1>
    <Color id="babyBlue" r0="0.1" b0="0.7" g0="0.2" />
  </ColorGroup1>
</RootNode>
```
