The dataset contains images from AVSS 2007 datset for abandoned luggage - http://www.eecs.qmul.ac.uk/~andrea/avss2007_d.html and CAVIAR surveillance dataset - http://homepages.inf.ed.ac.uk/rbf/CAVIARDATA1/ . We have used the ground truth labels (xmls) and extracted frames from these videos and classified them into the following categories

1. Abandoned (luggage unattended, our class of interest)
	> Train
	> Validate
	> Test	
2. Background (background, class of non-iterest)
	> Train
	> Validate
	> Test

**We have also applied image transformations like Flipped Orientation, Grayscale etc.. to increase our training/validation/test dataset**

---

Properties of our dataset
* 9.3 GB dataset
* 65,000 images
* 30,000 abandoned luggage
* 35,000 background images 

Link to our dataset - https://drive.google.com/file/d/0B6XbSjc8SWZ2RmV2alFVU0Vpcjg/view?usp=sharing