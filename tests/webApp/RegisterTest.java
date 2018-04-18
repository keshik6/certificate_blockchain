import org.openqa.selenium.By;
import org.openqa.selenium.WebDriver;
import org.openqa.selenium.WebElement;
import org.openqa.selenium.chrome.ChromeDriver;

public class RegisterTest {
	public static void main(String[] args) throws InterruptedException {
		//Usernames generated using python Faker library
		String[] userNames = {"jared68","paula06","moralesthomas","gdavis","huynhsean","hgonzalez","andrew38","nwhite","patricia54","samantha35","lbrown","smithcrystal","tperry","phillipbarnes","tiffany98","piercemark","jenniferdougherty","solisdouglas","morrisondale","melissajackson",};
		
		//Set the location of the chromedriver as the second argument
		System.setProperty("webdriver.chrome.driver","C://Users/user/Desktop/Term 5/50.003/Week 6/chromedriver.exe");
		WebDriver driver = new ChromeDriver();

		//Get the page
		driver.get("http://127.0.0.1:8000");
		driver.manage().window().maximize();
		
		System.out.println("Starting automated registration test");
		for (int i = 0; i< userNames.length; i++) {
			
			System.out.println("Iteration = " + (i+1) + " : Starting registration");
			//Go to the register page
			driver.navigate().to("http://127.0.0.1:8000/main_web_portal/register/");
			Thread.sleep(1000);
			
			String username = userNames[i];
			
			//This password is default
			String password = "Ethcert.io";
			
			//This email is my email which I can use for testing
			String email = "keshik6@gmail.com";
			
			//Get the username, email and password fields from the webpage
			WebElement usernameField = driver.findElement(By.name("username"));
			WebElement emailField = driver.findElement(By.name("email"));
			WebElement passwordField = driver.findElement(By.name("password"));
			
			//Send username and password to fill up the fields
			usernameField.sendKeys(username);
			emailField.sendKeys(email);
			passwordField.sendKeys(password);
			
			//Click the button to sign-in
			WebElement clickButton = driver.findElement(By.name("submit"));
			clickButton.click();
			System.out.println("Iteration = " + (i+1) + " : Completed registration");
			
			Thread.sleep(10000);
			
		}
		System.out.println("automated registration test complete");
	}
}
