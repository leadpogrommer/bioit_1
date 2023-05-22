FROM apache/airflow:latest
USER root
RUN apt-get update && DEBIAN_FRONTEND=noninteractive apt-get install -y freebayes minimap2 fastqc bwa samtools

# RUN pacman -Syu --noconfirm python python-pip samtools bwa fastqc minimap2 freebayes


# ENV AIRFLOW_HOME=/airflow
# ENV AIRFLOW_VERSION=2.6.1


# RUN pip install "apache-airflow==${AIRFLOW_VERSION}" --constraint "https://raw.githubusercontent.com/apache/airflow/constraints-${AIRFLOW_VERSION}/constraints-$(python --version | cut -d " " -f 2 | cut -d "." -f 1-2).txt"
# 
# RUN ln -sf /usr/share/zoneinfo/Asia/Novosibirsk /etc/localtime

# because freebayes devs do heavy drugs
# RUN mkdir -p /usr/lib/gcc/x86_64-pc-linux-gnu/12.2.1

ADD process.sh /usr/bin

RUN mkdir /host 
WORKDIR /host

USER 50000
RUN AIRFLOW__CORE__LOAD_EXAMPLES=False airflow db init && airflow users  create --role Admin --username q --email q --firstname admin --lastname admin --password q

# RUN mkdir -p /airflow
ADD dags /opt/airflow/dags

CMD [ "standalone" ]