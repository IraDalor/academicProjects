// A Java program for a Client 
import java.net.*; 
import java.io.*; 
import java.util.*;


  
public class Client 
{ 
    private long totaltime;
    // initialize socket and input output streams 
    private Socket socket            = null; 
    private long timemsec[] = new long[101];
    private String Request =null;
    	public Client(String address, int port) 
    { 
		System.out.println("enter number of clients : ");
    Scanner scanr = new Scanner(System.in);
    int numclient = scanr.nextInt();

        // establish a connection 
        try
        { 
           
  
          
  
        	ClientThread[] clie = new ClientThread[101];
    		
          
       	 // string to read message from input 
            String line = ""; 
            
           Scanner scan = new Scanner(System.in);
            boolean cont = false;
            
		do
		{
            	System.out.println("1. Host current Date and Time \n2. Host uptime \n3. Host memory use\n4. Host Netstat \n5. Host current users \n6. Host running processes \n7. Quit \n");
            	System.out.println("Enter a number.  ");
            	
                line = scan.nextLine();
                int val = Integer.parseInt(line);
       		Request  = line;
            	 if (val == 7)
	            {
	               cont = true;
	 
	             }
		      
           	 for (int x = 0; x < numclient; x++)
            	{
			socket = new Socket(address, port); 
            		clie[x] =  new ClientThread (socket);
            	}
		 System.out.println("Connected"); 
		 for (int x = 0; x < numclient ; x++)
            	   {	
			clie[x].start();
		
            	   }
		 System.out.println("Getting Info..."); 
            	  for (int x = 0; x < numclient; x++)
		  {
			
				try {
					clie[x].join();
				} catch (InterruptedException e) {
					// TODO Auto-generated catch block
					e.printStackTrace();
				}
				
			
		  }
		
		
		socket.close();
            	Socket socketDisplay = new Socket (address, port);
		DataOutputStream out   = new DataOutputStream(socketDisplay.getOutputStream()); 
       		PrintWriter write = new PrintWriter(out,true);
		InputStream input  = socketDisplay.getInputStream();
		BufferedReader read = new BufferedReader(new InputStreamReader(input));
	
			
        	write.println(Request);
				
		String Reply;
		while ((Reply = read.readLine()) != null)
		{
			System.out.println(Reply);
			//Reply = read.readLine();
		}
		
		socketDisplay.close();	
            }while(cont != true);
             	
		
		

		
			
            

			
        } 
        catch(UnknownHostException u) 
        { 
            System.out.println(u); 
        } 
        catch(IOException i) 
        { 
            System.out.println(i); 
        } 
   

       
    } 
  
    public static void main(String args[]) 
    { 
	
		System.out.println("Please enter the hostname:");
		Console read =  System.console();
		String Hostname = read.readLine();
        	Client client = new Client(Hostname, 5000); 

    } 
    
    

public class ClientThread extends Thread{
	
	private Socket socket;
	private InputStream input = null;
	private	DataOutputStream out  = null;
	public ClientThread(Socket socket) {
		this.socket = socket;
		}
	
	public void run()
	{
		//keep reading until 7
	     try
         {   // sends output to the socket 

       		out   = new DataOutputStream(socket.getOutputStream()); 
       		PrintWriter write = new PrintWriter(out,true);
		input  = socket.getInputStream();
		BufferedReader read = new BufferedReader(new InputStreamReader(input));
		long startTime = System.currentTimeMillis();
			
        	write.println(Request);
				
		String Reply;
		while (read.readLine() != null)
		{			
			Reply = read.readLine();
		}
            	long Finishtime = System.currentTimeMillis();
	     	long timeElapsed =  Finishtime - startTime;
            	System.out.println("Respond Time:" + timeElapsed + " msec");
	        totaltime += timeElapsed;
           	
		
			
         } 
         catch(IOException i) 
         { 
             System.out.println(i); 
         } 
 
} 

	}
	
}

    