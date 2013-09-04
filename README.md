wp_img_mover
============

This script identifies src property from `<img>` tags in .md files, copies the image file to Dropbox (if they were hosted on your Wordpress server), and changes the `<img>` tags to .md format. 


Usage: 

0. Install [Python](http://www.python.org/) and [lxml](http://lxml.de/).

1. Download the images hosted on your Wordpress site. 

   Connect to your host via ftp. You may find the images in something like /wp-content/uploads 


2. Edit the script `wp_img_mover.py` to set the correct urls / paths in lines 9-13. 

   `srcUrlPrefix`: prefix of the original image src url, excludes the part "year/mo/imagename.jpg", 

      e.g. 'http://azaleasays.com/wp-content/uploads/' 

   `destUrlPrefix`: prefix of the Dropbox url where you would like to host the image, 

      e.g. 'https://dl.dropboxusercontent.com/u/308058/blogimages/'

   `srcImgDirPrefix`: directory on your local machine where you temporarily store the downloaded images from Wordpress. 

      e.g. '/Users/azalea/Downloads/uploads/'

   `destImgDirPrefix`: directory under Dropbox's Public folder where you would like to store the images. 

      e.g. '/Users/azalea/Dropbox/Public/blogimages/'

   `postsDir`: directory where your jekyll blog posts are located. i.e. _posts

      e.g. '/Users/azalea/Dropbox/projects/azalea.github.io/_posts/' 


3. Create a test branch for your Jekyll project. 
 

4. Run the script by: 

      `python wp_img_viewer.py` 
 

5. Check very carefully to see if everything is ok. 

   If so, merge the test branch to master. 

   If not, edit the script at your will and retry.
   
   
Known issues:

Sometimes, text near the `<img>` tags may be truncated. 

   
