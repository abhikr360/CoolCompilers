class Main inherits IO {
	i : Int;
	a : Int[3];
    main() : Int {
		{

	    i <-0;
		a[0]<- 1;
		a[1]<- 2;
		a[2]<- 3;
		if i<=3 then
			a[i]<-a[i]+1
		else 
		fi;
		if i>=2 then
			a[i]<-a[i]-1
		else 
			a[i]<-1
		fi;
		}
    };
};
