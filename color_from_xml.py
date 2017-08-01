import sys, getopt
import xml.etree.ElementTree as ET

def generate_file(infile,sku):
    lower_sku = sku.lower()+'_' if sku is not '' else ''
    tree = ET.parse(infile)
    root = tree.getroot()

    class_body_arr = []
    class_header_arr = []
    for child in root:
        get_interface = generate_objc_interface_getter(lower_sku)
        get_method = generate_objc_method_getter(lower_sku)
        class_header_arr.extend(map(get_interface, child))
        class_body_arr.extend(map(get_method, child))
    class_m_base = r'#import "UIColor+'+sku+'Color.h"'+'\n\n'  \
                 +r'@implementation UIColor ('+sku+'Color)'+'\n\n'

    class_h_base = r'#import </UIKit/UIKit.h>'+'\n'  \
                   + r'@interface UIColor ('+sku+'Color)\n'

    class_h_body = '\n'.join(class_header_arr)
    class_m_body = '\n'.join(class_body_arr)
    class_end = '\n@end\n'

    class_m = class_m_base+class_m_body+class_end
    class_h = class_h_base+class_h_body+class_end
    write_to_file('UIColor+'+sku+'Color.m', class_m)
    write_to_file('UIColor+'+sku+'Color.h', class_h)

# args code based on https://www.tutorialspoint.com/python/python_command_line_arguments.htm
def main(prog_args):
    inputfile = ''
    sku = 'MY' 
    try:
        opts, args = getopt.getopt(prog_args,"hi:s:",["ifile=","sku="])
    except getopt.GetoptError:
        print_help()
        sys.exit(2)

    for opt, arg in opts:
        if opt == '-h':
            print_help()
            sys.exit()            
        elif opt in ("-i", "--ifile"):
            inputfile = arg
        elif opt in ("-s", "--sku"):
            sku = arg
    generate_file(inputfile,sku)

    
def get_objc_color(attr):
    return r'[UIColor colorWithRed:'+attr['r0']  \
    +r' green:'+attr['g0']  \
    +r' blue:'+attr['b0']+r'];'

def get_objc_method_name(sku_prefix,color_name):
    return '+ (UIColor *)'+sku_prefix+color_name

def get_color_from_elt(elt):
    color_name = elt.attrib.get('id', None)
    if color_name is None:
        sys.exit("Must supply an variable name (key 'id') for each xml color")
    return color_name    

def generate_objc_method_getter(sku_prefix):
    def get_objc_method(row):
        color_code = get_objc_color(row.attrib)
        color_name = get_color_from_elt(row)
        return get_objc_method_name(sku_prefix,color_name)  \
            +r' {'+'\n'  \
            +'\treturn '+color_code  \
            +'\n}'
    return get_objc_method

def generate_objc_interface_getter(lower_sku):
    def get_objc_interface(row):
        return get_objc_method_name(lower_sku, get_color_from_elt(row))+';'
    return get_objc_interface


def print_help():
    print(sys.argv[0]+' -i <inputfile> [-s <class SKU>]')

def write_to_file(filename, str):
    file = open(filename, 'w')
    file.write(str)
    print('Created ',filename)

main(sys.argv[1:])
