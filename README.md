# install wegiht2cpp
```
pip install weight2cpp
```

# c language app
```
#include <stdio.h>
#include <math.h>

float mdw[5][][]={
...
};

int ln=5;
int ls[5]={1, 2, 2, 3, 1};
int latf[5]={0,1,0,3,0}; //Input Activation Function num; latf[0]= input layer
//int model_struct={1, 2, 2, 3, 1};
//int Layers, Rows, Clms = 5, 5, 3;

float atReLu(float node_value);
float atSgmoid(float node_value);
float atTanh(float node_value);
float predict_cal();

int main()
{
    int l, r, c, mxclm=0;
    float rst;
  
    rst = predict_cal();
    
    for(l=0; l<ln; l++){ if(mxclm < ls[l]){ mxclm=ls[l]; }};

    for(l=0; l<ln; l++){
      for(r=0; r<mxclm+2; r++){
        for(c=0; c<mxclm; c++){ printf("%1.8f ",mdw[l][r][c]);}
      printf("\n");
      }
      printf("ls %d %d\n",ls[l],ls[l+1]);
    }

    printf("Prediction value = %1.8f \n", rst);
    return 0;
}

float predict_cal()
{ 
    int l, r, c;
    float n_vl,  n_vlt;
    int lrr[100];

    lrr[0]=1;
    for(l=1; l<ln; l++){lrr[l]= ls[l-1] + 2;} //get node value row on layer 

    for(l=1; l<ln; l++){

        for(c=0; c< ls[l]; c++){ 
            n_vl =0.0;
            for (r=0; r< ls[l-1]; r++){
                n_vl = n_vl + mdw[l-1][lrr[l-1]-1][r] * mdw[l][r][c];
            }
            n_vl = n_vl + mdw[l][r][c];
            
            if(latf[l]==1){
                n_vlt=atReLu(n_vl); 
                mdw[l][r+1][c]= n_vlt;
                //printf("lvr %d %f %f \n",l, n_vl,n_vlt);
            }
            else if(latf[l]==2){
                n_vlt=atSgmoid(n_vl); 
                mdw[l][r+1][c]= n_vlt;
            }
            else if(latf[l]==3){
                n_vlt=atTanh(n_vl); 
                mdw[l][r+1][c]= n_vlt;
            }      
            else{n_vlt=n_vl; mdw[l][r+1][c]= n_vl;}
        }
    }
    return n_vlt;
}

float atReLu(float node_value){ //1
    if(node_value > 0.){ return node_value; }
    return 0.;
} 

float atSgmoid(float node_value){ //2
    return 1/(1+exp(-node_value));
}

float atTanh(float node_value){ //3
    return tanhf(node_value);
}
```


