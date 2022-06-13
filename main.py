import os, sys, time
from datetime import datetime
import pandas as pd

def task_ram():
	tus = int(time.time()*10**6)
	fdir = os.environ['tmp'] + '\process' + str(tus) + '.csv'
	c = 'tasklist /v /fo csv > ' + fdir
	os.system(c)
	return fdir

def ram_grp(fdir, n=5):
	encodings = ['utf-8', 'gbk']
	for e in encodings:
		try:
			df = pd.read_csv(fdir, encoding=e)
			df['Mem Usage'] = df['Mem Usage'].str.replace(r'\D+', '', regex=True).astype(int)
			df_sum = df.groupby('Image Name')['Mem Usage'].sum()
			topn_gb = df_sum.sort_values(ascending=False).head(n).div(1024**2).round(1).apply(lambda x: str(x) + ' GB')
		except:
			pass

	print(topn_gb)

def main():
	stime = time.time()
    # Optional parameter: topN
	fdir = task_ram()
	if len(sys.argv) > 1:
		n = int(sys.argv[1])
		ram_grp(fdir, n)
	else:
		ram_grp(fdir)
	# timestamp
	dt = datetime.now()
	print('End time:', dt)
	# run time
	print('Run time:', round(time.time()-stime,3), 's')

if __name__ == '__main__':
	main()
