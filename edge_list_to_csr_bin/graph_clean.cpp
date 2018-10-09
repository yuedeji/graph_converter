/**
 * input: edge_list
 * function: remove redundant edges, remove self-cycle
 * output: new_edge_list
**/

#include <stdio.h>
#include <algorithm>
#include <set>

using namespace std;

void clean_graph(int args, char **argv)
{
    const char * file_in = argv[1];
    const char * file_out = argv[2];
    printf("%s, %s\n", file_in, file_out);
    int u, v;
    FILE * fp_in = fopen(file_in, "r");
    FILE * fp_out = fopen(file_out, "w");

    set<int> st;
    int prev_u = -1;
    int sum_self = 0;
    int sum_redundant = 0;
    while(fscanf(fp_in, "%d%d", &u, &v) != EOF)
    {
//        printf("%d, %d", u, v);
        if(prev_u == u)
        {
            if(st.find(v) != st.end())
            {
                sum_redundant ++;
                continue;
            }
            else
            {
                if(u != v)
                {
                    st.insert(v);
                    fprintf(fp_out, "%d %d\n", u, v);
                }
                else
                {
                    sum_self ++;
                }
            }
        }
        else
        {
            prev_u = u;
//            printf("set size = %d\n", st.size());
            st.clear();
            st.insert(v);
            if(u != v)
                fprintf(fp_out, "%d %d\n", u, v);
            else
                sum_self ++;
        }
    }
    fclose(fp_in);
    fclose(fp_out);
    printf("redundant, %d, self cycle, %d\n", sum_redundant, sum_self);
}
int main(int args, char **argv)
{
    if(args != 3)
    {
        printf("Usage: ./graph_clean <input_edge_list> <output_edge_list>\n");
        exit(1);
    }
    clean_graph(args, argv);

    return 0;
}
