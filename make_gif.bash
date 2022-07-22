function recursive_for_loop { 
    for f in *;  do 
        if [ -d $f  -a ! -h $f ];  
        then  
            cd -- "$f";  
            echo "Creating gif in `pwd`/$f"; 
	    convert -delay 40 -loop 0 *.png animation.gif
            # use recursion to navigate the entire tree
            recursive_for_loop;
            cd ..; 
        fi;  
    done;  
};

recursive_for_loop
