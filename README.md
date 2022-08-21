<!-- TABLE OF CONTENTS -->
<details>
  <summary>Table of Contents</summary>
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
    <li><a href="#performance">Performance</a></li>
    <li><a href="#future enhancements">Future Enhancements</a></li>
    <li><a href="#contributing">Contributing</a></li>
    <li><a href="#license">License</a></li>
    <li><a href="#acknowledgments">Acknowledgments</a></li>
  </ol>
</details>



<!-- ABOUT THE PROJECT -->
## About The Project

<a href="https://drive.google.com/uc?export=view&id=15sUxappbBKoIgjKnC_V2PiugkUe1_QNp"><img src="https://drive.google.com/uc?export=view&id=15sUxappbBKoIgjKnC_V2PiugkUe1_QNp" style="width: 400px; max-width: 100%; height: auto"  /></a>


This program allows users to take multiple CSV files and change the order of the columns to their liking. Users can create and save file configurations to use again in the future.

This program would be useful for users who:
* Want to change the order of or delete columns from multiple CSV files.
* Have files with different column orders and want them all to be the same format.
* Want to remove unnecessary columns from files too big for Microsoft Excel to handle.

Go from:  
<a href="https://drive.google.com/uc?export=view&id=1Mf8yv_dYLQyo39yx2mJMYG8FCGMsAqrh"><img src="https://drive.google.com/uc?export=view&id=1Mf8yv_dYLQyo39yx2mJMYG8FCGMsAqrh" style="width: 500px; max-width: 100%; height: auto"  /></a>

To:  
<a href="https://drive.google.com/uc?export=view&id=12hdYyzP3nUCtroQkLw2gDNubKQameXW7"><img src="https://drive.google.com/uc?export=view&id=12hdYyzP3nUCtroQkLw2gDNubKQameXW7" style="width: 500px; max-width: 100%; height: auto"  /></a>

<p align="right">(<a href="#readme-top">back to top</a>)</p>



### Built With

* Python
* Tkinter
* Pandas


<!-- GETTING STARTED -->
## Getting Started



### Prerequisites

You will need:
* [Python 3.7+](https://www.python.org/downloads/)
* The Pandas Library
```sh
pip install pandas
```
For more help installing Python packages, please visit: [https://packaging.python.org/en/latest/tutorials/installing-packages/](https://packaging.python.org/en/latest/tutorials/installing-packages/)


### Installation

1. Download the code from this repo as a ZIP file and extract the contents wherever you want to execute the main file.
2. Open a command prompt/terminal window in the directory the main.py file lives.
3. Run the below command
   ```sh
   python main.py
   ```

<p align="right">(<a href="#readme-top">back to top</a>)</p>



<!-- USAGE EXAMPLES -->
## Usage

* The 'Column Name' column is where you will enter the name you want shown on the output file.
* The 'Column # from file' column is the integer index of the column from the input file. Counting starts from 1. i.e., A=1, B=2, etc.
* The 'Header row' box is where you will enter the row where the headers/column names exist on the input file. Counting starts from 1. 
* If more columns past 'E' are needed you can press the '+' at the bottom of the screen to add up to 21 additional columns for a maximum of 26 columns on the output file.
  
  
* Once your configuration is created you can save it by giving it a name in the input box at the bottom of the screen and clicking 'Save'
* The configuration will then appear in the 'Select Configuration' drop down at the top of the screen so it can be used in the future. 
  
  
* Once ready to process files, click 'Browse' and select as many CSV files as needed and click 'Process File'
* Your output files will appear in the same directory as the main.py folder with unique names.


<p align="right">(<a href="#readme-top">back to top</a>)</p>



<!-- Performance -->
## Performance

The amount of time it will take for files to be processed will be dependent on how many files need to be processed and the size of the files as well as the hardware the program is being run on. Generally, for files with 1,000 rows, the program can process about 80 files per second. For larger files, you can expect somewhere around 200,000 rows to be processed per second thanks to the efficiency of the Pandas library.


<!-- Future Enhancements -->
## Future Enhancements

- [ ] Modern looking UI
- [ ] Edit existing configs
- [ ] Delete existing configs
- [ ] Filter rows depending on a user given condition
- [ ] Create new columns with the result of an operation performed on input file's column(s). i.e., column A + column B


<p align="right">(<a href="#readme-top">back to top</a>)</p>



<!-- CONTRIBUTING -->
## Contributing

Contributions are what make the open-source community such an amazing place to learn, inspire, and create. Any contributions you make are **greatly appreciated**.

If you have a suggestion that would make this better, please fork the repo and create a pull request. You can also simply open an issue with the tag "enhancement".
Don't forget to give the project a star! Thanks again!

1. Fork the Project
2. Create your Feature Branch (`git checkout -b feature/AmazingFeature`)
3. Commit your Changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the Branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

<p align="right">(<a href="#readme-top">back to top</a>)</p>



<!-- LICENSE -->
## License

Distributed under the MIT License. See `LICENSE.txt` for more information.

<p align="right">(<a href="#readme-top">back to top</a>)</p>



<!-- ACKNOWLEDGMENTS -->
## Acknowledgments

* Othneil Drew for his [README Template](https://github.com/othneildrew/Best-README-Template)

<p align="right">(<a href="#readme-top">back to top</a>)</p>



