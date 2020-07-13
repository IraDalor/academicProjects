import java.util.Scanner;

public class Bank {
	private int allocation[][], maximum[][], need[][], available[], cust, res;
	
	private void addCustomer()
	{
		Scanner s = new Scanner(System.in);
		System.out.print("Enter number of customers: ");
		cust = s.nextInt();
		System.out.print("Enter amount resources: ");
		res = s.nextInt();
		need = new int[cust][res];
		maximum = new int[cust][res];
		allocation = new int[cust][res];
		available = new int[res];
		
		System.out.println("Enter allocation matrix");
		for (int i = 0; i < cust; i++)
			for (int j = 0; j < res; j++)
				allocation[i][j] = s.nextInt();
		
		System.out.println("Enter maximum matrix");
		for (int i = 0; i < cust; i++)
			for (int j = 0; j < res; j++)
				maximum[i][j] = s.nextInt();
		
		System.out.println("Enter available resources: ");
		for (int j = 0; j < res; j++)
			available[j] = s.nextInt();
		
		s.close();
	}
	
	private int[][] getNeed()
	{
		for (int i = 0; i < cust; i++)
			for (int j = 0; j < res; j++)
				need[i][j] = maximum[i][j] - allocation[i][j];
		return need;
	}
	
	private boolean isSafe(int i)
	{
		for(int j = 0; j < res; j++)
			if(available[j] < need[i][j])
				return false;
		
		return true;
	}
	
	public void getState()
	{
		addCustomer();
		getNeed();
		boolean fin[] = new boolean[cust];
		int i = 0;
		
		while(i < cust)
		{
			boolean al = false;
			for(int j = 0; j < cust; j++)
				if(!fin[j] && isSafe(j))
				{
					for(int k = 0; k < res; k++)
						available[k] = available[k] - need[j][k] + maximum[j][k];
					al = true;
					fin[j] = true;
					i++;
				}
			    if(!al)
			    	break;				
		}
		if(i == cust)
			System.out.println("Safe");
		else
			System.out.println("Not safe");
	}
	
	public static void main(String[] args)
	{
		new Bank().getState();
	}
}
