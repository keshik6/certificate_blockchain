
import java.net.HttpURLConnection;
import java.net.MalformedURLException;
import java.net.URL;

import org.openqa.selenium.By;
import org.openqa.selenium.JavascriptExecutor;
import org.openqa.selenium.Keys;
import org.openqa.selenium.StaleElementReferenceException;
import org.openqa.selenium.WebDriver;
import org.openqa.selenium.WebElement;
import org.openqa.selenium.chrome.ChromeDriver;
import org.openqa.selenium.firefox.FirefoxDriver;
import org.openqa.selenium.support.ui.ExpectedConditions;
import org.openqa.selenium.support.ui.WebDriverWait;

public class CheckBrokenLinks {
	
	// this is a function which checks whether a given hyper link in a web page is broken
	public static void brokenLinkChecker(URL hyperLink) throws Exception {
		
		String acknowledge = null;
		HttpURLConnection linkConnection = (HttpURLConnection) hyperLink.openConnection();

		try {
			System.out.println("*** Checking link " + hyperLink.toString());
			
			// initiate an HTTP connection
		    linkConnection.connect();
		    
		    // check whether the connection is responding
		    acknowledge = linkConnection.getResponseMessage();
		    
		    // disconnect the connection link
		    linkConnection.disconnect();
		    System.out.println("*** The link " + "returned " + acknowledge);
		} catch(Exception e) {
		    System.out.println("*** The link " + "is broken, message = " + acknowledge);
		}  				
	}
		
	public static void main(String[] args) throws Exception {
		//Set the location of the chromedriver as the second argument
		System.setProperty("webdriver.chrome.driver","C://Users/user/Desktop/Term 5/50.003/Week 6/chromedriver.exe");
		WebDriver driver = new ChromeDriver();

		driver.get("http://127.0.0.1:8000");

		// get all the links
		java.util.List<WebElement> links = driver.findElements(By.tagName("a"));
		//System.out.println(links.size());
		
		System.out.println("Index\tLink Text\t\tLink URL");
		// print all the links
		for (int i = 0; i < links.size(); i=i+1) {
			if (links.get(i).getText().isEmpty()) {
				continue;
			}
		
			//Print the links in neat format
			if (links.get(i).getText().contains("\n")) {
				System.out.print(i + "\t" + links.get(i).getText().replaceAll("\n", ""));
			}
			else {
				System.out.print(i + "\t" + links.get(i).getText());
			}
			System.out.println("\t" + links.get(i).getAttribute("href"));
		}
		
		// call broken link checker for all the links found
		for (int i = 0; i < links.size(); i=i+1) {
			try {
				brokenLinkChecker(new URL(links.get(i).getAttribute("href")));
			} catch (Exception e) {
				System.out.println("This is not a proper URL to connect to " + links.get(i).getAttribute("href"));
			}
		}
		
		System.out.println("Broken Links test completed");
		driver.close();
	}
}
