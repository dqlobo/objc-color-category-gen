# objc-color-category-gen
Python script that generates a category class of UIColor in Objective C. Works great with exported XML files from [Paletton](http://paletton.com/). See Format for details.

# Background
I love creating my app color schemes on [Paletton](http://paletton.com/), but hate wasting time writing stupid color categories. Paletton has an export to XML button, so I wrote a python script so I NEVER HAVE TO WRITE A COLOR CATEGORY AGAIN!

# Usage
```
> python3 color_from_xml.py -i<inputfile> -s<SKU>
```
Notes:
* Requires Python 3
* outputs to current directory
* SKU is whatever your iOS app SKU is (See [here](http://lmgtfy.com/?q=what+is+app+sku) for details)

# Format
This script just traverses and XML file and extracts properties that correspond to color name and rgb (as floats). The format is as follows:
```
<RootNode>
  <ColorGroup1>
    <Color id="crimson" r0="0.7" b0="0.2" g0="0.2" />
    <Color id="lighterCrimson" r0="1" b0="0.2" g0="0.2" />
  </ColorGroup1>
  <ColorGroup2>
    <Color id="babyBlue" r0="0.1" b0="0.7" g0="0.2" />
  </ColorGroup2>
</RootNode>
```
