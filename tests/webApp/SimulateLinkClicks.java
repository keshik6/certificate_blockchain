import java.util.List;

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

public class SimulateLinkClicks{
		
	public static void main(String[] args) throws InterruptedException {		
		System.setProperty("webdriver.chrome.driver","C://Users/user/Desktop/Term 5/50.003/Week 6/chromedriver.exe");
		WebDriver driver = new ChromeDriver();

		driver.get("http://127.0.0.1:8000");
		
		// get all the links
		java.util.List<WebElement> links = driver.findElements(By.tagName("a"));
		
		//Print the table
		System.out.println("Index\tLink Text\t\tLink URL");
		
		// print all the links
		for (int i = 0; i < links.size(); i=i+1) {
			//If link text is empty then it is null link
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
		
		driver.manage().window().maximize();
		
		
		// click all links in a web page
		for(int i = 0; i < links.size(); i++)
		{
			
			if (links.get(i).getAttribute("href") == null)
				continue;
			else {
				System.out.println("*** Navigating to" + " " + links.get(i).getAttribute("href"));
			}
			while(true) {
				try {
					String link = links.get(i).getAttribute("href");
					driver.navigate().to(link);
					Thread.sleep(3000);
					if (!link.equals("http://127.0.0.1:8000/")) {
						driver.navigate().back();
					}
					links = driver.findElements(By.tagName("a"));
					break;
				} catch (StaleElementReferenceException e) {
					System.out.println("***Error is here");
				}
			}
		}
		System.out.println("Click Simulation Test completed successfully");
		driver.close();
		
	}
	
	
}
