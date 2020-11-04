 <p align="center"><img src="https://media2.giphy.com/media/IJN8K3ogDXbh657ZBV/giphy.gif" width="220" height="200"> </p>
<h1 align="center"> Visual AI </h1>
<br>
<p align="center">Visual is a AI that uses machine learning to understand the interest of a user with data that is obtained, to in turn generate topics the user probally likes.</p>
<br>

<h2> Usage</h2>

<p>To use Visual you need to follow the steps of installation. Visual is intended to collect data so the service provider can create reliable suggestions. We advise that Visual is used for only applications and or websites. To get it running you need to link a source for the JSON (more down below). When you have it linked to a source and it is storing data for you in the JSON file, you can start the Visual. Now you wait so the AI can do its work.</p>

<p><b> Disclaimer: Visual is still work in progress. We do not support any misuse of Visual.</b></p>
<p align="center"><img src="https://media4.giphy.com/media/ondcObRzXHxIANFAJ0/giphy.gif" width="480" height="234"> </p>

<h2> Known problems</h2>
<pre>
 -The JavaScript function not totally functional yet.
 -The PHP doesnt write the data correctly to the JSON file
 -The machine learning barely used
 -There arent exception catchers, what in turn makes Visual very unstable</pre>
 
<h2> Supported</h2>
 <p>All languages down below is supported from Visual. We want to give the user/developer as easy time as possible so we created files/code for the user/developer to use with Visual. These files can be found inside the InfoInjector folder.</p>
 <h4> JavaScript</h4>
 <p>To use the injector for JavaScript you can add the function to another file that gets info. From there you can call the function with the string name that the function needs.</p>
 <pre> InfoInjectors\JavaScript_Injector.js </pre>
 <h4> PHP</h4>
 <p>To implement this injector you need to have a input named "data". The form were the input is placed needs to have a reference to the injector.</p>
 <pre> InfoInjectors\PHP_Injector.php </pre>
 <p> All files are not finished yet </p>

## Building
To build Visual you need:
- A clone/release of Visual

<h2> Installation</h2>
  <h3> Visual</h3>
  <ul>
   <li>Link the WordKeeper.py script to a source that can enter data for it (or another source that can put data inside data.json)</li>
   <li>Run the Visual.py script</li>
   <li>Let it keep running</li></ul>
  <p> If Visual.py script says "List Of Topics Has Been Adjusted", it means that the AI is running.</p>
<h2> Storyboard</h2>
  <pre>
  - Create project (✔)
  - Make a python script that can be accessed to add data to some kind of storage (✔)
  - Make a script that generates a list of intrest based on the most used words/terms. (✔)
  - Create a AI/Program to generate the most accurate intrest list all the time (✔)
  - Introduce machine learning for a better process (✔)
  - Develop more in machine learning for better quality
  - Create more storyboard points</pre>
  
<h2> Sources</h2>
<ul>
  <li>https://www.oracle.com/nl/artificial-intelligence/what-is-machine-learning.html</li>
  <li>https://docs.python.org/3/</li>
  <li>https://docs.python.org/3/library/json.html</li>
</ul>



