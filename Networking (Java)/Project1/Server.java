import java.io.*;
import java.net.*;
import java.util.Date;
public class Server {

	 //initialize socket and input stream 

	private int numClient = 0;
    // constructor with port 
    public Server(int port) 
    { 
        // starts server and waits for a connection 
        try
        { 
           ServerSocket server = new ServerSocket(port); 
            System.out.println("Server started"); 
  
            System.out.println("Waiting for a client ..."); 
            
            while (true)
            {
            	Socket socket = server.accept(); 
               numClient +=1;
            
               System.out.println("Client accepted");
            	
            	new ServerThread (socket).start();
            	
            }
			
        
        } 
        catch(IOException i) 
        { 
            System.out.println(i); 
        } 
    } 
  

    public static void main(String args[]) 
    { 
        Server server = new Server(5000); 
    }
    
    
    public class ServerThread extends Thread {

    	private Socket socket;
      
    	
    	public ServerThread(Socket socket) {
    		this.socket = socket;
    		}
    	
    	public void run() 
    	{
    		try
    		{
    			// takes input from the client socket 
    			InputStream in  = socket.getInputStream();
            	BufferedReader read = new BufferedReader(new InputStreamReader(in)); 
    			OutputStream out = socket.getOutputStream();
    			PrintWriter write = new PrintWriter(out,true);
    		        long startTime = System.currentTimeMillis();
    	         long elapsedTime;

            	String line = ""; 
            	String X="";
            	String reply;
             	 BufferedReader input = null;
            	Process p;
       
            	
                    	line = read.readLine();
         do{           
                      switch(line){                   
                      case "1":    
                      System.out.println("User requested date and time.");
                       break;
                      case "2":
                     System.out.println("User requested uptime.");
                     break;
                     case "3":
                        System.out.println("User requested memory usage.");
                     break;
                     case "4":
                         System.out.println("User requested netstat.");
                       break;
                       case "5":
                        System.out.println("User requested current users.");
                        break;
                     case "6":
                         System.out.println("User requested running processes.");
                           break;
                     default:
                     ;
                     break;
                     }

                           
                     
		do
		{	
                  
                 
                  switch (line) {
  	                    case "1": 
                          p = Runtime.getRuntime().exec("date");
  	                    	 input = new BufferedReader(
  	                    			 new InputStreamReader(p.getInputStream()));
  	                   

  	                    	break;
  	                    case "2": 
  	                  
                         p = Runtime.getRuntime().exec("uptime");
  	                    	 input = new BufferedReader(
  	                    			 new InputStreamReader(p.getInputStream()));
  	                      	                        
  	                    	break;
  	                    case "3": 
                    

  	                    	 p = Runtime.getRuntime().exec("free");
  	                    	 input = new BufferedReader(
  	                    			 new InputStreamReader(p.getInputStream()));
                           	                    	break;
  	                    case "4": 
  	                    	
                           p = Runtime.getRuntime().exec("netstat");
	                    		input = new BufferedReader(new InputStreamReader(p.getInputStream()));
					                                     
  	                    	break;
  	                    case "5": 
  	                    	
                           p = Runtime.getRuntime().exec("who");
  	                    		input = new BufferedReader(new InputStreamReader(p.getInputStream()));  	               
  	                     
                         System.out.println("Sent: " + p);
                       	break;
  	                    case "6": 
  						 	     
  	                    		p = Runtime.getRuntime().exec("ps -e");
  	                    		input = new BufferedReader(new InputStreamReader(p.getInputStream()));
					              	                    	break;
  	                    case "7": 
  	                    	System.out.println("Closing Connection");
  	                    	line = "7";
  	                    	break;
  	                    default:
  	                    	line = "er";
  	                    	break;
  	                    }
                    	
              if (line == "7")
			 {
				write.println("Closing Connection");
			 }
			 else if (line == "er")
			 {
				write.println("Invalid Choice");
  			 }
			 else
			 {
			 
  			 	while ((reply = input.readLine()) != null) 
			               {
				              write.println(reply); // <-- Print all Process here line
												// by line
					
			                }
  			  input.close();
			 }
              socket.close();
            	in.close();
            	out.close();
        

		}while (line !=  "7");
      }while (line !=  "7"); 	
           }
    	catch (IOException ex) {
    		
    	}
    		
    	}
    }

}  


