# **Exploratory Data Analysis (EDA) App**

## **Introduction**

The Exploratory Data Analysis (EDA) App is a Streamlit-based web application that allows users to perform comprehensive exploratory data analysis on their datasets. This app provides an intuitive and user-friendly interface for uploading CSV files, visualizing the input data, and generating an interactive profiling report.

## **Key Features**

- **File Upload:** Users can upload their CSV datasets using the file uploader in the sidebar.
- **Data Visualization:** The uploaded dataset is displayed on the main page, allowing users to preview the data.
- **Profiling Report Generation:** The app uses the ydata-profiling library to generate an interactive profiling report for the uploaded dataset. This report provides detailed insights and visualizations about the data.
- **Responsive Design:** The app is designed with a responsive layout, ensuring a seamless user experience across different screen sizes.
- **Example Dataset:** If no file is uploaded, the app provides an example dataset for users to explore the app's functionality.

## **How to Use the App**

### **Step 1: Upload a CSV File**

1. In the sidebar, click the "Upload your CSV file" section.
2. Use the file uploader to select your CSV dataset.
3. Once the file is uploaded, the app will display the input DataFrame.

### **Step 2: Generate the Profiling Report**

1. After uploading the dataset, the app will automatically generate a profiling report.
2. The profiling report is displayed in the main section of the app, providing comprehensive insights and visualizations about the data.
3. Users can scroll through the report to explore the various sections, such as dataset overview, variable descriptions, and correlation analysis.

### **Step 3: Explore the Profiling Report**

1. The profiling report is interactive, allowing users to interact with the visualizations and explore the data in depth.
2. Users can expand or collapse different sections of the report to focus on specific aspects of the data.
3. The report includes a wide range of analyses, including data types, missing values, univariate and bivariate analyses, and more.

## **Code Walkthrough**

[https://github.com/muhammadadilnaeem/Practice-Projects/assets/162784706/ecead803-c26a-4b65-99df-2b3175d93ec1](https://github.com/muhammadadilnaeem/Practice-Projects/assets/162784706/8fdc2bf1-80f8-43c0-852e-6016890d66b7)

### **Importing Libraries**

The app starts by importing the necessary libraries, including Streamlit, Pandas, NumPy, and the ydata-profiling library for generating the profiling report.

### **Setting Page Configuration**

The app sets the page configuration using `st.set_page_config()`, which includes the page title, layout, and initial sidebar state.

### **Adding CSS Styling**

The app adds some custom CSS styles to enhance the user interface, such as setting the background color and adjusting the padding of various elements.

### **Creating the App Structure**

The app is structured with a title, an image, and instructions in the sidebar. The main content area is divided into two sections: the input DataFrame and the profiling report.

### **Handling File Upload**

The app includes a file uploader in the sidebar, which allows users to upload their CSV files. When a file is uploaded, the app loads the data using the `load_data()` function, which is cached for better performance.

### **Generating the Profiling Report**

The app uses the `generate_profile_report()` function, which is also cached, to generate the profiling report for the uploaded dataset. The report is then displayed in the main content area using Streamlit's `components.html()` function.

### **Providing an Example Dataset**

If no file is uploaded, the app offers an example dataset that users can explore. The example dataset is generated and cached using the `load_example_data()` function.

## **Conclusion**

The Exploratory Data Analysis (EDA) App provides a user-friendly and efficient way for users to perform comprehensive data exploration on their datasets. By leveraging the power of Streamlit and the ydata-profiling library, the app generates detailed and interactive profiling reports, enabling users to gain valuable insights into their data.
