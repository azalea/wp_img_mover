import os
import glob
import re
from StringIO import StringIO
from lxml import etree
from lxml.html import builder as E


srcUrlPrefix = 'http://azaleasays.com/wp-content/uploads/'
destUrlPrefix = 'https://dl.dropboxusercontent.com/u/308058/blogimages/'
srcImgDirPrefix = '/Users/azalea/Downloads/uploads/'
destImgDirPrefix = '/Users/azalea/Dropbox/Public/blogimages/'
postsDir = '/Users/azalea/Dropbox/projects/azalea.github.io/_posts/'


def replaceUrl(src, srcUrlPrefix=srcUrlPrefix, destUrlPrefix=destUrlPrefix):
    return src.replace(srcUrlPrefix, destUrlPrefix)

def copyImg(src, srcUrlPrefix=srcUrlPrefix, srcImgDirPrefix=srcImgDirPrefix, destImgDirPrefix=destImgDirPrefix):
    longpath = src.replace(srcUrlPrefix, '')
    subpath, filename = longpath.rsplit('/', 1)
    destImgDir = destImgDirPrefix + subpath
    os.system('test -d %s || mkdir -p %s && cp -n %s%s %s%s'%(destImgDir, destImgDir, srcImgDirPrefix, longpath, destImgDirPrefix, longpath))

def processPost(postpath):
    parser = etree.HTMLParser(encoding='UTF-8')
    f = open(postpath, 'r+b')

    tree = etree.parse(f, parser)
    for src in tree.xpath("//img/@src"):
        #print src
        srctxt = re.sub(r'(^\S+\.[A-Za-z]{3,4})\?w=\d{2,4}', r'\1', src)
        #print srctxt
        md = '\n![](%s)\n'%replaceUrl(srctxt)
        if srcUrlPrefix in srctxt:
            copyImg(srctxt)
        par = src.getparent() 
        if par.getparent().tag == 'a':  # if <img> is inside <a>
            par.getparent().getparent().replace(par.getparent(), E.P(md))
        else:                           # if <img> is not inside <a>
            par.getparent().replace(par, E.P(md))

    etree.strip_tags(tree, 'p', 'html', 'body')

    output = etree.tostring(tree, encoding='UTF-8')
    leadinghtml = '<!DOCTYPE html PUBLIC "-//W3C//DTD HTML 4.0 Transitional//EN" "http://www.w3.org/TR/REC-html40/loose.dtd">\n<html>'
    trailinghtml = '</html>'
    output = output.replace(leadinghtml,'').replace(trailinghtml,'')
    output = output.replace('&#13;', '')
    f.seek(0)
    f.write(output)
    f.truncate()
    f.close()

for filename in glob.glob('%s*.md'%postsDir):
#    if filename == postsDir+'test.md':
#        print filename
    processPost(filename)
