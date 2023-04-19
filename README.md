> Project Under Construction

Authors

[Aswin Lal M](https://www.linkedin.com/in/aswnss)   
[Bhavagath Mohan](mailto:bhagavathmani2016@gmail.com)   
[Hashir P Anwer](mailto:hashirpanwer@gmail.com)

# Fake Logo Detection Using Machine Learning

The proposed mini project aims to develop a system that can detect fake or plagiarized logos using a reverse image search approach. The system will compare the given logo with a database of authentic logos to find the best match. The similarity between the logos will be determined using similarity metrics such as cosine similarity or mean squared error.The system will flag the given logo as fake or plagiarized if the level of similarity with any of the logos in the database is above a certain threshold, such as 90%.The developed system will be useful for companies and organizations to protect their brand identity and intellectual property rights by detecting unauthorized use of their logos.

## Technology Used

1. Pretrained ImageNetV2 Model
2. Perceptual Hashing
3. Siamese Image Similarity
4. Large Logo Dataset

## Dataset
1.  [Large Logo Dataset](https://data.vision.ee.ethz.ch/sagea/lld/data/LLD-logo_files.zip)
2.  [WIPO Logos](https://drive.google.com/drive/folders/1VXE0FWqLQDJijI8FeFN2v9gy8jA6cfGa?usp=share_link)
3.  [Brand Logos](https://www.kaggle.com/datasets/kkhandekar/popular-brand-logos-image-dataset)

## Installing the Project

1. Creating a virtualenv
    ```
    pip install virtualenv
    virtualenv venv
    ```
2. Activating Virtualenv
    ```
    ./venv/Scripts/activate
    ```
3. Installing requirements
    ```
    pip install -r requirements.txt
    ```

## References

1. Vivek Tanniru,Tathagata Bhattacharya “Online Fake Logo Detection System”- 2023
2. I Gede Susrama Mas Diyasa,Alfath Daryl Alhajir,Amir Muhammad Hakim,Moh. Fathur Rohman “Reverse Image Search Analysis Based on
Pre-Trained Convolutional Neural Network Model”,2020 Information Technology International Seminar (ITIS)
3. Alexander Sage, Eirikur Agustsson, Radu Timofte, Luc Van Gool “Logo Synthesis and Manipulation with Clustered Generative Adversarial Networks”,
4. Pratamamia Agung Prihatmaja, Reverse Image Search Using Pre Trained Deep Learning Model, [Read the blog](https://medium.com/swlh/reverse-image-search-using-pretrained-deep-learning-model-83f16ef4aec8)

