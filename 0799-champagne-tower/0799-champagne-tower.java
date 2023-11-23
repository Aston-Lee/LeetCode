class Solution {
    public double champagneTower(int poured, int query_row, int query_glass) {
        

        float[][] tower = new float[query_row+2][];
        for (int i=0; i<query_row+2; i++) {
            tower[i] = new float[i+1];
            Arrays.fill(tower[i], 0);
        }
        
        float remain = 0;
        tower[0][0] = poured;
        for (int r=0; r<query_row+1; r++) {
            for (int g=0; g<=r; g++) {
                // System.out.println(r+" "+g+" "+tower[r][g]);
                if (tower[r][g] > 1) {
                    remain = tower[r][g] - (float)1.0;
                    tower[r+1][g] += remain / 2;
                    tower[r+1][g+1] += remain / 2;
                }
            }
            // System.out.println("---");
        }
        
        return Math.min(1, tower[query_row][query_glass]);
    }
}