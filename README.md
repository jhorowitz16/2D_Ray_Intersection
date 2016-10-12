# 2D_Ray_Intersection
2D Ray Intersection with Asynchronous Sampling Frequencies



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
