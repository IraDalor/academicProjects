Specifications for the project are as follows, the project functioned as expected per specification:

Write a program in Java which creates producer and consumer threads. The producer should “produce” by setting the elements of an array of integers to FULL. The consumer should “consume” by setting the elements of an array of integers to EMPTY. 

Make sure you properly handle the following situations:

  A producer (consumer) producing (consuming) past the end (beginning) of the buffer

  A producer writing to an array element that is not EMPTY and a consumer reading (i.e. setting the array element to EMPTY) from an array element that is not FULL.

  Use wait() and notify() to avoid errors producing and consuming and to ensure thread synchronization.
