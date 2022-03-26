# Numpy_Rubik
this is the base of a rubik cube that uses numpy


  This class was made because of an idea that I had in mind to try
and create a solution from scratch of how to create a rubik's cube
in numpy and be able to keep track of the colors on the faces. the 
reason hat it does not work with a normal cube of (N x N x N) is because
each element represents a smaller cube within the cube and does not
provide any additional orientation data. Now I was thinking about 
trying to code a system that does so and keeps the axis information
and updates them with every rotation but it seemed like to complicated
of a solution.

  The idea of the solution that I had though up is to put one layer on each
  side of the cube to represent the colors. This solution makes the cube bigger
  within numpy but is more easily understandable. This solution creates a cube
  with the new dimensions (N+2 x N+2 x N+2).
  
  
  What is currently lacking is the ability to retrieve the current faces of 
  the cube due to the format of the returned object being too specific based
  on the use case of the cube.


