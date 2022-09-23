no=1
number=10
echo debug1
while [ $no -le $number ]
do
echo debug2
no=$((no+1))
done
echo debug3