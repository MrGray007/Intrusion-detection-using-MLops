import streamlit as st
import json
import pandas as pd
from col_trans import dropcol,col_name
import pickle as pk
from pipeline.deployment import predictor_loader
import numpy as np
from time import sleep

def main():
    def time_filter(df):
        return df.Timestamp.str.replace(r'\d{2}/\d{2}/\d{4}\s+', '', regex=True)
    file=st.file_uploader('Upload CSV File', type='csv')
    if file is not None:
        pipe=pk.load(open(r'/mnt/c/Users/mahesh/Desktop/zenml_wsl/pipeline.pkl','rb'))
        pipeline_name="continous_deployment";pipeline_step_name="mlflow_model_deployer_step"
        service=predictor_loader(pipeline_name=pipeline_name,step_name=pipeline_step_name,running=True)
        #service.start(timeout=30)
        if service is None:
            print('No service found')
        df=pd.read_csv(file)
        src_ip=df['Src IP']
        df=df.drop(columns='Src IP')
        time=time_filter(df)
        test=pipe.transform(df)
        print(test)
        service.start(timeout=30)
        json_list=json.loads(json.dumps(list(test.T.to_dict().values())))
        test=np.array(json_list)
        res=service.predict(test)
        out=pd.DataFrame(data={'time':time,"ip":src_ip,'Attacks':res})
        labels={ 5:'Infilteration',
             3:'Benign',
             1:'DoS',
             2:'DDoS',
             0:'Bot',
             4:'Brute Force',
             2:'DDOS'}
        out['Attacks']=out['Attacks'].map(labels)
        out=out.sort_values(by='time')
        st.header('Insights of Data:')
        st.metric(label='Total columns',value=len(df.columns))
        st.metric(label='Total Rows',value=len(out))
        st.metric(label='Total IP',value=out['ip'].nunique())
        st.write('Count of Label:')
        st.dataframe(out['Attacks'].value_counts())
        attack=out[out['Attacks']!='Benign']
        attack['con_ip']=((attack['ip']!=attack['ip'].shift())).cumsum()
        ip_grp=attack['con_ip'].value_counts()
        ip=ip_grp[ip_grp>=2]
        att_ip=attack[attack['con_ip'].isin(ip)]['ip'].values
        print(att_ip)
        st.divider()
        if len(att_ip)>=1:
            st.warning(f'Watch out!⚠️ {",".join(att_ip)} trying to attack')
        else:
            st.success("No attack Spoted")


        if st.button('Generate graph:'):
            with st.spinner('Genrating Graph.....'):
                sleep(3)
            # st.header('Time Vs Label')
            # fig = px.line(out, x='time', y='label', title='Time vs Label')
            # st.plotly_chart(fig)

            # plt.figure(figsize=(10, 6))
            # sns.lineplot(data=out, x='time', y='label', marker='o', linestyle='-', color='b')
            # # Customize plot
            # plt.title('Time vs. Label (Seaborn)')
            # plt.xlabel('Time')
            # plt.ylabel('Label')
            # plt.xticks(rotation=45)
            # st.pyplot(plt)
            out=out.set_index('time')
            print(out)
            st.line_chart(out['label'].astype('str'))

if __name__=='__main__':
    main()







