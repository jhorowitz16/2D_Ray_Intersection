# 2D_Ray_Intersection
2D Ray Intersection with Asynchronous Sampling Frequencies


Update: I am currently using 'argparse' to take in all the parameters for the experiment up front. The parameters (in the following order) are as shown below *in order*. All parameters are floats with the exception of the two device names.

device_a
 - name
 - x coordinate of initial position
 - y coordinate of initial position
 - initial angle (in radians using a polar coordinate convention)
 - noise constant (to add some variance to the calculations)
 - turn speed (in radians per time step, with positive speeds for counterclockwise and negative speeds for clockwise)
 - polling frequency (in Hz)
 
 Then the same 7 arguments but for device_b 
 
 Lastly the experiment parameters
  - The monitor frequency (in Hz)
  - number of time steps to display (just for the experiment)
  
In total there are 16 parameters (7 per device, 2 for environment). A screenshot is included demonstrating this intermediate product.


=====

My plan for this project is to take it in stages.



Stage 1: Simple Python Calculator
 * the purpose here is to experiment with the math behind the ray calculations
 * python function takes:
  - both devices positions
  - two lists of angle measurements (polar coordinate angle)
    * for now, just take the average of those measurements as the true angle
 * return the (x, y) coordinate of their intersection or report no intersection
 
 
 
Stage 2: Sampling Frequencies
  * Instead of doing the math with two "true" angles, break down the problem into time intervals based on the frequencies
  * My idea here is to break the problem down into time steps
   - a time step is the least common dominator of the time-between-measurements of the two devices
   - get time-between-measurements based on frequencies
   - for points in time without doubt - interpolate (for now at least take the average of the two closest points)
  * Now we iterate through the our two lists of measurements (both the same length b/c both in terms of the LCD time step)
   - For each pair of measurements - calculate the rays intersection and report
   - the frequency of these reports is the rate of the overall system
   
Stage 3: UI
  * TBD, but ideally something better than plain text input / output
