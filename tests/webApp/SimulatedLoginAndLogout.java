import org.openqa.selenium.By;
import org.openqa.selenium.WebDriver;
import org.openqa.selenium.WebElement;
import org.openqa.selenium.chrome.ChromeDriver;

public class SimulatedLoginAndLogout {
	public static void main(String[] args) throws InterruptedException {	
		//Set the location of the chromedriver as the second argument
		System.setProperty("webdriver.chrome.driver","C://Users/user/Desktop/Term 5/50.003/Week 6/chromedriver.exe");
		WebDriver driver = new ChromeDriver();

		//Get the page
		driver.get("http://127.0.0.1:8000");
		driver.manage().window().maximize();
		
		//Go to the login page
		driver.navigate().to("http://127.0.0.1:8000/main_web_portal/user_login/");
		Thread.sleep(1000);
		
		//Username and password for an account
		String name = "keshik";
		String password = "Ethcert.io";
		
		//Get the username and fields from the webpage
		WebElement usernameField = driver.findElement(By.name("username"));
		WebElement passwordField = driver.findElement(By.name("password"));
		
		//Send username and password to fill up the fields
		usernameField.sendKeys(name);
		passwordField.sendKeys(password);
		Thread.sleep(1000);
		
		//Click the button to sign-in
		WebElement clickButton = driver.findElement(By.name("Login"));
		clickButton.click();
		
		System.out.println("Successfully logged in");
		
		Thread.sleep(1000);
		
		//Now log out
		driver.navigate().to("http://127.0.0.1:8000/main_web_portal/user_logout");
		
		System.out.println("Successfully logged out");
		
		driver.close();
		System.out.println("Login/Logout test successfull");

	}	
}
