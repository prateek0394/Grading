var markDict = {};
var RPlst2 = ['endDevelopmentReport','endDevelopmentPresentation','endResearchReport','endResearchPresentation'];
var RPlst1 = ['midProposalContent','midProposalPresentation','midDevelopmentReport','midDevelopmentPresentation','midResearchReport','midResearchPresentation'];
var Theslst1 =  ['viva1','midsemPresentation','midsemReport','viva2','finalThesis','finalViva'];
var Dislst1 = ['viva1','midsemPresentation','midsemReport','viva2','finalDissertation','finalViva'];
var Dislst2 = ['workProgress','technicalCompetence','documentation','initiative','puntuality','reliability'];
var Projlst1 =  ['midregularityMentor','projectViva1','projectViva2','weekdocumentSubmission','midsemViva','midsemReport']
var Projlst2 = ['endregularityMentor','projectViva34','finalSeminar','finaldocumentSubmission'];
var Theslst2 = ['writtenAbstract','technicalContent','depthKnowledge','stylePresentation','responseQuestion'];
var Theslst3 = ['workProgress','technicalCompetence','documentation','initiative','puntuality','reliability'];
markDict['endDevelopmentReport'] = 10;
markDict['endDevelopmentPresentation'] = 5;
markDict['endResearchReport'] = 20;
markDict['endResearchPresentation'] = 15;
markDict['midDevelopmentReport'] = 5;
markDict['midDevelopmentPresentation'] = 10;
markDict['midResearchReport'] = 10;
markDict['midResearchPresentation'] = 10;
markDict['midProposalContent'] = 10;
markDict['midProposalPresentation'] = 5;
markDict['viva1'] = 15;
markDict['finalThesis'] = 25;
markDict['finalViva'] = 15;
markDict['midsemPresentation'] = 15;
markDict['midsemReport'] = 15;
markDict['viva2'] = 15;
markDict['finalDissertation'] = 25;
markDict['midregularityMentor'] = 10;
markDict['projectViva1'] = 5;
markDict['projectViva2'] = 5;
markDict['weekdocumentSubmission'] = 10;
markDict['midsemViva'] = 10;
markDict['midsemReport'] = 10;
markDict["endregularityMentor"] = 10;
markDict["projectViva34"] = 10;
markDict["finalSeminar"] = 15;
markDict["finaldocumentSubmission"] = 15;

function compare(val1,val2){
if(val1<=val2)
  return 1;
else
  return 0;

}

function validate(id,lst,ct){
var z = 1;
  var total=0;
  var i=0;
  for(i=0;i<lst.length;i++){
    if(document.getElementById(ct+lst[i]+id).value=="")
      document.getElementById(ct+lst[i]+id).value = 0;
    z = z&compare(parseInt(document.getElementById(ct+lst[i]+id).value),markDict[lst[i]]);
  if(z==0){
    alert('Incorrect Value(s)!!!\nMax value is '+markDict[lst[i]]);
    document.getElementById(ct+lst[i]+id).value = '0';
    document.getElementById(ct+lst[i]+id).focus();
  return -1*total;
  }
  total = total+parseInt(document.getElementById(ct+lst[i]+id).value);
} 
return total;
}

function openEdit(id,tn,ct,lst){
  for (var i = 0;i<lst.length ; i++) {
  document.getElementById(ct+lst[i]+id).removeAttribute('disabled');
  }
  document.getElementById(ct+'edit'+tn+id).style.display = 'none';
  document.getElementById(ct+'save'+tn+id).style.display = 'inline';
}

function closeEdit(id,tn,ct,lst){
  for (var i = 0;i<lst.length ; i++) {
  document.getElementById(ct+lst[i]+id).setAttribute('disabled',true);
 
  }
   document.getElementById(ct+'edit'+tn+id).style.display = 'inline';
  document.getElementById(ct+'save'+tn+id).style.display = 'none';

}

function createDict(lst,ct,id){
  dataDict = {};
  for(var i=0;i<lst.length;i++){
    dataDict[lst[i]] = document.getElementById(ct+lst[i]+id).value;
  }
  return dataDict;
}

function submitData(dataDict,url){
  dataDict["data"] = JSON.stringify(dataDict["data"]);
  $.getJSON(url, dataDict, function(data, jqXHR){
    if(data[0]==='OK'){
       alert('Submiited Successfully');

       return 1;
}else{
  alert('Error Occurred!! Try again or Contact Developers');
  return 0;
}
});
}
//----------------------------------------------------------------------------------------------------------------
//Research Practice Code
function RPedit(id,tn){
  if(tn=='1')
{  openEdit(id,tn,3,RPlst1);
document.getElementById('3midsemGrade'+id).removeAttribute("disabled");
}else
 { openEdit(id,tn,3,RPlst2);
  document.getElementById('3endsemGrade'+id).removeAttribute("disabled");
}
}

function RPsave(id,tn){
var x;
var tabname;
  if(tn=='1'){
    x = RPlst1;
    tabname = 'MidSemEvaluation';
  }
  else{
    x = RPlst2;
    tabname = 'EndSemEvaluation';
  }
var t = validate(id,x,3);
if(t<0)
  return false;
var dataDict = createDict(x,3,id);
if(tn=='1'){
  dataDict["midsemTotal"] = t;
}else{
  dataDict["endsemTotal"] = t;
  var t1 = validate(id,RPlst1,3);
  if(t1<0)
    return false;
  dataDict["Total"] = t+t1;
}

finalData = {'id':id,'tabname':tabname,'data':dataDict,'midsemGrade':document.getElementById('3midsemGrade'+id).value,'endsemGrade':document.getElementById('3endsemGrade'+id).value};
submitData(finalData,'/grade/marks');

  closeEdit(id,tn,3,x);
if(tn=='1')
  document.getElementById('3midsemGrade'+id).setAttribute("disabled",true);
else
  document.getElementById('3endsemGrade'+id).setAttribute("disabled",true);
}
function RPtotal(id,tn){
  if(tn=='1'){
    document.getElementById('3midsemTotal'+id).innerHTML = Math.abs(validate(id,RPlst1,3));
  }else{
        document.getElementById('3endsemTotal'+id).innerHTML = Math.abs(validate(id,RPlst2,3));
        document.getElementById('3Total'+id).innerHTML = Math.abs(validate(id,RPlst2,3))+parseInt(document.getElementById('3midsemTotal'+id).innerHTML);
  }
}
//Research Practice Code ends
//------------------------------------------xxxxxxxxx-------------------------------------------------------------------

//----------------------------------------------------------------------------------------------------------------------
//Thesis code 

function Thesistotal(id,tn){
  if(tn=="1"){
    document.getElementById('4Total'+id).innerHTML = Math.abs(validate(id,Theslst1,4));
  }
}
function Thesedit(id,tn){
  if(tn=="1"){
    openEdit(id,tn,4,Theslst1);
    document.getElementById('4midsemGrade'+id).removeAttribute("disabled");
    document.getElementById('4endsemGrade'+id).removeAttribute("disabled");
    document.getElementById('4seminarGrade'+id).removeAttribute("disabled");
  }
  else if(tn=="2"){
    openEdit(id,tn,4,Theslst2);
  }else if(tn=="3"){
    openEdit(id,tn,4,Theslst3);
  }
}
function Thessave(id,tn){
  var finalData = {};
  var dataDict = {};
  var tabname;
  var x;
  var y;
  var ny;
  if(tn=="1"){
    ny = id;
    y = "1";
    tabname = "Evaluation";
    x = Theslst1;
    dataDict = createDict(Theslst1,4,id);
    dataDict["seminarGrade"] = document.getElementById('4seminarGrade'+id).value;
    var t = validate(id,Theslst1,4);
    if(t<0)
      return false;
    dataDict["Total"]= t;
   
  }else if(tn=="3"){
    ny = id;
    y= "3";
    x  = Theslst3;
    tabname = "StudentTraits";
    dataDict = createDict(Theslst3,4,id);
  }else{
    y = "2";
    ny = id+tn;
x = Theslst2;
    if(tn=="S1"){tabname="Seminar1";}else if(tn=="S2"){tabname="Seminar2";}else if(tn=="S3"){tabname="Seminar3";} else if(tn=="S4"){tabname="Seminar4";}
    dataDict = createDict(Theslst2,4,id+tn);
}
 finalData = {'id':id,'tabname':tabname,'data':dataDict,'midsemGrade': document.getElementById('4midsemGrade'+id).value,'endsemGrade': document.getElementById('4endsemGrade'+id).value};
submitData(finalData,'/grade/marks');
 closeEdit(ny,y,4,x);
if(tn=='1'){
  document.getElementById('4midsemGrade'+id).setAttribute("disabled",true);
  document.getElementById('4endsemGrade'+id).setAttribute("disabled",true);
  document.getElementById('4seminarGrade'+id).setAttribute("disabled",true);

}
}
//Thesis Code ends
//------------------------------------------xxxxxxxxx-------------------------------------------------------------------

//----------------------------------------------------------------------------------------------------------------------
//Dissertation code 

  function Dissersave(id,tn){
var x;
var finalData = {};
var dataDict = {};
var tabname;
if(tn=="1"){
tabname = "Evaluation";
dataDict = createDict(Dislst1,2,id);
x = Dislst1;
 var t = validate(id,Dislst1,2);
if(t<0)
   return false;
dataDict["Total"]= t;
}else{
tabname = "StudentTraits";
x = Dislst2;
dataDict = createDict(Dislst2,2,id);
}
finalData = {'id':id,'tabname':tabname,'data':dataDict,'midsemGrade':document.getElementById('2midsemGrade'+id).value,'endsemGrade':document.getElementById('2endsemGrade'+id).value};
submitData(finalData,'/grade/marks');
 closeEdit(id,tn,2,x);
if(tn=='1'){
  document.getElementById('2midsemGrade'+id).setAttribute("disabled",true);
  document.getElementById('2endsemGrade'+id).setAttribute("disabled",true);
}
}
function Disseredit(id,tn){
if(tn=="1"){
openEdit(id,tn,2,Dislst1);
document.getElementById('2midsemGrade'+id).removeAttribute("disabled");
document.getElementById('2endsemGrade'+id).removeAttribute("disabled");
}else{
openEdit(id,tn,2,Dislst2);
}
 }
function Dissertotal(id,tn){
 if(tn=="1"){
    document.getElementById('2Total'+id).innerHTML = Math.abs(validate(id,Dislst1,2));
  }
}
//Dissertation Code ends
//------------------------------------------xxxxxxxxx-------------------------------------------------------------------

//----------------------------------------------------------------------------------------------------------------------
//Projects code 
function Projtotal(id,tn){
if(tn=="1"){
  document.getElementById('1midsemTotal'+id).innerHTML = Math.abs(validate(id,Projlst1,1));
}else{
  document.getElementById('1Total'+id).innerHTML = Math.abs(validate(id,Projlst2,1))+parseInt(document.getElementById('1midsemTotal'+id).innerHTML);
}
}
function Projedit(id,tn){
if(tn=="1"){
  openEdit(id,tn,1,Projlst1);
  document.getElementById('1midsemGrade'+id).removeAttribute("disabled");
}else{
  openEdit(id,tn,1,Projlst2);
 document.getElementById('1endsemGrade'+id).removeAttribute("disabled");
}
}
function Projsave(id,tn){
  var x;
var finalData = {};
var dataDict = {};
var tabname;
if(tn=="1"){
  tabname = "MidSemEvaluation";
x = Projlst1;
dataDict = createDict(Projlst1,1,id);
var t = validate(id,Projlst1,1);
if(t<0)
  return false;
dataDict["midsemTotal"] = t; 
}else{
  tabname = "EndSemEvaluation";
x = Projlst2;
dataDict = createDict(Projlst2,1,id);
var t = validate(id,Projlst2,1);
if(t<0)
  return false;
dataDict["Total"] = t + parseInt(document.getElementById('1midsemTotal'+id).innerHTML); 
}
finalData = {'id':id,'tabname':tabname,'data':dataDict,'midsemGrade':document.getElementById('1midsemGrade'+id).value,'endsemGrade':document.getElementById('1endsemGrade'+id).value};
submitData(finalData,'/grade/marks');
closeEdit(id,tn,1,x);
if(tn=='1'){
  document.getElementById('1midsemGrade'+id).setAttribute("disabled",true);
}
  else{
  document.getElementById('1endsemGrade'+id).setAttribute("disabled",true);
}
}

//Projects Code ends
//------------------------------------------xxxxxxxxx-------------------------------------------------------------------

//-------------------------xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx--------------------------------------------