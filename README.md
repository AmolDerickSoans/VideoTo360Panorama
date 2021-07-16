
<!-- [![Contributors][contributors-shield]][contributors-url]
     [![Stargazers][stars-shield]][stars-url]
[![Contributors][contributors-shield]][contributors-url]
[![Forks][forks-shield]][forks-url]
[![Stargazers][stars-shield]][stars-url]
[![Issues][issues-shield]][issues-url]
-->




<!-- PROJECT LOGO -->
<br />
<p align="center">
  <a href="https://github.com/AmolDerickSoans/VideoTo360VR">
    <img src="resources/360-camera.png" alt="Logo" width="80" height="80">
  </a>

  <h3 align="center">VideoTo360Panorama</h3>

  <p align="center">
    OpenCV python based software to turn video clips into a single 360 panoroma image
    <br />
    <a href="https://github.com/othneildrew/Best-README-Template"><strong>Explore the docs »</strong></a>
    <br />
    <br />
    <a href="https://github.com/AmolDerickSoans/VideoTo360VR/issues">Report Bug</a>
    ·
    <a href="https://github.com/othneildrew/Best-README-Template/issues">Request Feature</a>
</p>



<!-- TABLE OF CONTENTS -->
<details open="open">
  <summary><h2 style="display: inline-block">Table of Contents</h2></summary>
  <ol>
    <li>
      <a href="#about-the-project">About The Project</a>
      <ul>
        <li><a href="#built-with">Built With</a></li>
      </ul>
    </li>
    <li>
      <a href="#getting-started">Getting Started</a>
      <ul>
        <li><a href="#prerequisites">Prerequisites</a></li>
        <li><a href="#installation">Installation</a></li>
      </ul>
    </li>
    <li><a href="#usage">Usage</a></li>
    <li><a href="#roadmap">Roadmap</a></li>
    <li><a href="#contributing">Contributing</a></li>
    <li><a href="#license">License</a></li>
    <li><a href="#contact">Contact</a></li>
    <li><a href="#acknowledgements">Acknowledgements</a></li>
  </ol>
</details>



<!-- ABOUT THE PROJECT -->
## About The Project  
   Convert multiple Videos Shot into single 360 panoramic Image using openCV image stitching.
[![VideoTo360Panorama][product-screenshot]](https://github.com/AmolDerickSoans/VideoTo360VR/blob/main/resources/mainWindowV1.PNG)
[![Page1]][product-screenshot1]](https://github.com/AmolDerickSoans/VideoTo360VR/blob/main/resources/mainWindowV1.PNG)


<!--Here's a blank template to get started:
**To avoid retyping too much info. Do a search and replace with your text editor for the following:**
`github_username`, `repo_name`, `twitter_handle`, `email`, `project_title`, `project_description`

-->
### Built With

* [Python 3.9.5]()
* [OpenCv 4.5.2]()
* [Tkinter]()



<!-- GETTING STARTED -->
## Getting Started

To get a local copy up and running follow these simple steps.

### Prerequisites

This is  list of python packages you need to use the software and how to install them.
* pip
  ```sh
   pip install opencv-contrib-python
   pip install pillow
   pip install matplotlib
   pip install imutils
  ```

### Installation

1. Clone the repo
   ```sh
   git clone https://github.com/AmolDerickSoans/VideoTo360Panorama.git
   ```
2. Install pip packages mentioned above
3. Run
   ```sh
   python OpenCV360v1.00.py 
   ```
4. TroubleShooting : 1. make sure output/vid1 output/vid2 output/vid3 directories are made.
                     2. to delete the blurred images python requires file permissions set up properly
   


<!-- USAGE EXAMPLES -->
## Usage

1. Select 3 short video files
2. Set the number of frames you want to skip
3. Click on "next"
4. You can view the console for which frames are being picked and which ones are deleted for being blurred
5. output is stored in output directory


_For more examples, please refer to the [Documentation](https://example.com)_

<!--FEATURES-->
- [x] Frame Extraction from video input
- [x] Blur Detection and deletion of blurred frames
- [ ] Preview Extracted Frames
- [x] Multi-threading to optimise speed
- [x] Panorama Stitching using SIFT
- [ ] Panorama Viewer 


<!--OUTPUT-->


<!-- ROADMAP -->
## Roadmap

See the [open issues](https://github.com/github_username/repo_name/issues) for a list of proposed features (and known issues).




<!-- CONTRIBUTING -->
## Contributing

Contributions are what make the open source community such an amazing place to be learn, inspire, and create. Any contributions you make are **greatly appreciated**.

1. Fork the Project
2. Create your Feature Branch (`git checkout -b feature/AmazingFeature`)
3. Commit your Changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the Branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request



<!-- LICENSE -->
## License

Distributed under the MIT License. See `LICENSE` for more information.



<!-- CONTACT -->
## Contact

Your Name - [@twitter_handle](https://twitter.com/twitter_handle) - email

Project Link: [https://github.com/github_username/repo_name](https://github.com/AmolDerickSoans/VideoTo360VR/issues)



<!-- ACKNOWLEDGEMENTS -->
## Acknowledgements

* [Richi Susil Jacob]()
* []()
* []()





<!-- MARKDOWN LINKS & IMAGES -->
<!-- https://www.markdownguide.org/basic-syntax/#reference-style-links -->
[contributors-shield]: https://img.shields.io/github/contributors/othneildrew/Best-README-Template.svg?style=for-the-badge
[contributors-url]: https://github.com/github_username/repo/graphs/contributors
[forks-shield]: https://img.shields.io/github/forks/othneildrew/Best-README-Template.svg?style=for-the-badge
[forks-url]: https://github.com/AmolDerickSoans/VideoTo360Panorama/network/members
[stars-shield]: https://img.shields.io/github/stars/othneildrew/Best-README-Template.svg?style=for-the-badge
[stars-url]: https://github.com/AmolDerickSoans/VideoTo360VR/stargazers
[issues-shield]:  https://img.shields.io/github/issues/othneildrew/Best-README-Template.svg?style=for-the-badge
[issues-url]: https://github.com/AmolDerickSoans/VideoTo360Panorama/issues
[license-shield]: https://img.shields.io/github/license/othneildrew/Best-README-Template.svg?style=for-the-badge
[license-url]: https://github.com/github_username/repo/blob/master/LICENSE.txt
[linkedin-shield]: https://img.shields.io/badge/-LinkedIn-black.svg?style=for-the-badge&logo=linkedin&colorB=555
[linkedin-url]: https://linkedin.com/in/github_username
[product-screenshot]: resources/startpage.PNG
[product-screenshot1]: resources/page1.PNG
[output]: resources/result.JPG
