demoFile="parsey/syntaxnet/demo.sh"
smdemoFile="parsey/syntaxnet/smdemo.sh"
contextFile="parsey/syntaxnet/models/parsey_mcparseface/context.pbtxt"

if [ -f "$demoFile" ]
then
	cp $demoFile $smdemoFile
	sed -i '40,56 d' $smdemoFile
	sed -i '39s/\\//' $smdemoFile
	sed -i -e 's/=bazel-bin/=parsey\/bazel-bin/g' $smdemoFile
	sed -i -e 's/=syntaxnet/=parsey\/syntaxnet/g' $smdemoFile
	echo "$smdemoFile has been modified."
else
	echo "$demoFile not found."
fi

if [ -f "$contextFile" ]
then
	sed -i -e 's/"syntaxnet/"parsey\/syntaxnet/g' $contextFile
	echo "$contextFile has been modified."
else
	echo "$contextFile not found."
fi

