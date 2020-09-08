# FacialVerificationSystem
End to end Facial Verification system where we verify if 2 images have to same face

Facial Verification is different then Facial Recognition. Facial recognition is when given an image, you need to match that image against all images in the database and the highest match is our image i.e it is 1:N matching. Facial verification is a 1:1 matching if it is the same person in 2 images.
Facial verification can be a challengng task as we have just one image in trainingg data per class(Each person).

Steps

(1)  Please follow the setup to download face_recognition python package
(2)  Get 2 different folders with a list of photos you want to match. Note there should be exactly 2 photos of the same person and should have the same name in 2 separate folder. Sample data format is given in the folders- BH_CAMP and BH_REGP. Please ensure that each image has just one face in it.
(3)  Specify the name of the folders
(4)  Specify the sensitivity (Between 0-1). Sensitivity of 0.1 means 2 images are more similar to each other then sensitivity of 0.2. So the lower the sensitivity you specify, the more number of True Positive. But this would also increase the False Negatives. Basically, reducing it to 0.1 would give a more confident match. I recomment using it as 0.5 - 0.6
(5) Allow the code to run. After it runs, you will see 2 HTML page generated: Matched.html and NoFaceDetected.html

Matched.html- All matching photos
NoFaceDetected.html: All Unmatched images and images where the model wasn't able to detect a face due to various reasons like blurred image, lack of lighting or multiple face detected in a single picture etc.
