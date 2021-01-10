Alexandre FORESTIER / Julie PICOT

# One word about the iPythonNotebook

* All the datanalysis part has been done in the file *dataexploration.ipynb* please open this file with vscode and python extension enabled as jupyter is missing half of our diagramms. be carefull if you're executing this file it will take sevral hours before you get all the results (thank you k fold cross validation). We advise you to have a look at our results

# WebSite startup and requirements

* The file requirement.txt contains all the libraries required to run our website which runs on django (if you really want to run the ipynb you will also need plotly and seaborn)
* To install all the required libraries set your current directory to the root of project and type ``` pip install -r requirements.txt ``` in your terminal
* To run the website move your current dirrectory to /WebSiteData  ``` cd WebSiteData ``` and then simply copy paste this command:
``` python manage.py runserver ```
* Head to [this link](http://127.0.0.1:8000/prediction/index/) and tadaaaaa :) 

# Conclusion

- This dataset was a challenging dataset
- First of all there was a lot missing data and it took us a lot of time before we could make tests with the integrality of the dataset
- Then our data was fragmented in several files depending on the year it was collected, we decided to keep this fragmentation and make 5 analysis (in fact one analysis generalized to all the others datasets in a later time)
- This approach was the right one as at the end we can see some differences on the variable importance between the different datasets. We have a great overall accuracy. But as there isn't that much bankrupted companies (thank you god) it is difficult for the model to catch up all the important points.
- In the website we do not ask enough variables to user which leads to extremely bad results


Here is a list of things we could have done (better):
* Duplicate the bankrupted data and add some noise add weight to this small class
* Focus less on hyperparameters optimization it took us a lot of both computational and personal time to get a moderate amelioration
* Remove some variables, we're used to remove insignificant variables in regressions but not in classification. This may come from the fact that our tree balances himself alone by choosing were he's cutting and that this step unnecessary.


Thank you for your attention Alexandre and Julie

