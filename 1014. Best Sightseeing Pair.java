// You are given an integer array values where values[i] represents the value of the ith 
//sightseeing spot. Two sightseeing spots i and j have a distance j - i between them.

// The score of a pair (i < j) of sightseeing spots is values[i] + values[j] + i - j: the sum of
//the values of the sightseeing spots, minus the distance between them.

// Return the maximum score of a pair of sightseeing spots.
class Solution {
    public int maxScoreSightseeingPair(int[] values) {
        int n=values.length;
        int max=-1;
        int[] suff=new int[n];
        suff[n-1]=values[n-1]-(n-1);
        for(int i=n-2;i>=0;i-=1){
            suff[i]=Math.max(suff[i+1],values[i]-i);
        }
        for(int i=0;i<n-1;i++){
            max=Math.max(suff[i+1]+i+values[i],max);
        }
        return max;

    }
}