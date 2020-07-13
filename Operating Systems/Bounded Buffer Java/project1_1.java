class Arr
{
    int size;
    int count = 0;
    int out = 0;
    int in = 0;
    int[] arr;
    
    public Arr(int size)
    {
    	if(size <= 0)
    	{
    		throw new IllegalArgumentException("size less than 0");
    	}
    	this.size = size;
    	arr = new int[size];
    }
    
    public synchronized void set(int num) throws InterruptedException
    {
    	while(count == size)
    	{
    		wait();
    		System.out.println("Array is full");
    	}
    	arr[in] = num;
    	in = (in + 1) % size;
    	count++;
    	notifyAll();
    }
    
    public synchronized int get() throws InterruptedException
    {
    	while (count == 0)
    	{
    		System.out.println("Array is empty");
    		wait();
    	}
    	int num = arr[out];
    	out = (out + 1) % size;
    	count--;
    	notifyAll();
    	return num;
    }
}

class Producer extends Thread
{
	final Arr arr;
	
	public Producer(Arr array)
	{
		arr = array;
	}
	
	public void run()
	{
		try
		{
			for(int num = 0; num <= 25; num++)
			{
				System.out.println("Produced: " + num);
				arr.set(num);
			}
		}catch(InterruptedException e) {}
	}
}

class Consumer extends Thread
{
	final Arr arr;
	
	public Consumer(Arr array)
	{
		arr = array;
	}
	
	public void run()
	{
		try
		{
			while (true)
			{
				int num = arr.get();
				System.out.println("Consumed: " + num);
			}
		}catch(InterruptedException e) {}
	}
}

public class project1_1
{
	public static void main(String[] args)
	{
		Arr arr = new Arr(5);
		Producer producer = new Producer(arr);
		Consumer consumer = new Consumer(arr);
		producer.start();
		consumer.start();
		try
		{
			producer.join();
			consumer.interrupt();
		}catch(InterruptedException e) {}
	}
}