#!/usr/bin/env python
# coding: utf-8

# In[ ]:


using System; 
 class HelloWorld 
 {   
     static void Main()   
     {       
         //variables to hold the task count and choices      
         int choice,task_count=0;      
         string[] tasks = new string[10];     
         //display the choices      
         while(true)
         {      
             Console.WriteLine("1.Add a task");      
             Console.WriteLine("2.View all tasks");      
             Console.WriteLine("3.Delete all tasks");      
             Console.WriteLine("4.Exit");      
             Console.Write("Enter your choice: ");      
             choice=Convert.ToInt32(Console.ReadLine());      
             //Implement the choices      
             switch(choice)      
             {
                 case 1:
                 {         
                     while(true)
                     {                 
                         string choice1;                 
                         //if the task_count is less than 10                 
                         if (task_count<10)                 
                         {                    
                             //Ask the task name                     
                             Console.Write("\nEnter the task name: ");                    
                             //add the task                      
                             tasks[task_count++]=Console.ReadLine();                    
                             Console.WriteLine("\nTask successfully added.\n ");                     
                             //prompt for adding other task                     
                             Console.Write("Do you want to add another task? [y/n] ");                     
                             choice1=Console.ReadLine();                     
                             //if choice y or Y then re prompt else break                    
                             if(choice1[0]=='y'||choice1[0]=='Y')                      
                             continue;                     
                             else                         
                             break;                 
                             
                         }                 
                         //if the tasks is full display the message                 
                         else                 
                         {                     
                             Console.Write("\nNo space for new task.");                     
                             break;                 
                             
                         }                         
                         
                     }             break;          
                     
                 }          
                 //for viewing the tasks added          
                 case 2:          
                 {             
                     //if the task count is not 0 the loop and display the tasks stored             
                     if(task_count!=0)              
                     {                 
                         int i;                 
                         Console.Write("\nThe task added are ...");                 
                         for(i=0;i<task_count;i++)                     
                         Console.Write("\n"+Convert.ToString(i+1)+". "+tasks[i]);              
                         
                     }             
                     //if not display no tasks added              
                     else                 
                     Console.Write("\nNo tasks available");             
                     break;          
                     
                 }          
                 //for deleting the tasks          
                 case 3:          
                 {              
                     int i=0;             
                     //assign all the assigned tasks to empty slots              
                     for(i=0;i<task_count;i++)                 
                     tasks[i]="";                 
                     //make the task count to 0              
                     task_count=0;              
                     Console.WriteLine("\nAll tasks cleared successfully.");              
                     break;          
                     
                 }          
                 //exit case          
                 case 4:             
                 {            
                     return;             
                     
                 }         
                 //default case         
                 

