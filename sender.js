var markDict = {};
var RPlst2 = ['endDevelopmentReport','endDevelopmentPresentation','endResearchReport','endResearchPresentation'];
var RPlst1 = ['midProposalContent','midProposalPresentation','midDevelopmentReport','midDevelopmentPresentation','midResearchReport','midResearchPresentation'];
var Theslst1 =  ['viva1','midsemPresentation','midsemReport','viva2','finalThesis','finalViva'];
var Dislst1 = ['viva1','midsemPresentation','midsemReport','viva2','finalDissertation','finalViva'];
var Dislst = ['workProgress','technicalCompetence','documentation','initiative','puntuality','reliability'];
var Prolst1 =  ['midregularityMentor','projectViva1','projectViva2','weekdocumentSubmission','midsemViva','midsemReport']
var Prolst2 = ['endregularityMentor','projectViva34','finalSeminar','finaldocumentSubmission'];
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
markDict["endregularityMentor"] = 10
markDict["projectViva34"] = 10
markDict["finalSeminar"] = 15
markDict["finaldocumentSubmission"] = 15

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
    z = z&compare(parseInt(document.getElementById(ct+lst[i]+id).value),markDict[lst[i]]);
  if(z==0){
    alert('Incorrect Value(s)!!!\nMax value is '+markDict[lst[i]]);
    document.getElementById(ct+lst[i]+id).value = '0';
    document.getElementById(ct+lst[i]+id).focus();
  return total;
  }
  total = total+parseInt(document.getElementById(ct+lst[i]+id).value);
} 
return total;
}

function openEdit(id,tn,ct,lst){
  for (var i = 0;i<lst.length ; i++) {
  document.getElementById(ct+lst[i]+id).removeAttribute('disabled');
  document.getElementById(ct+'edit'+tn+id).style.display = 'none';
  document.getElementById(ct+'save'+tn+id).style.display = 'inline';
  };
}

function closeEdit(id,tn,ct,lst){
  for (var i = 0;i<lst.length ; i++) {
  document.getElementById(ct+lst[i]+id).setAttribute('disabled',true);
  document.getElementById(ct+'edit'+tn+id).style.display = 'inline';
  document.getElementById(ct+'save'+tn+id).style.display = 'none';
  };
}

function RPedit1(id){
var RPlst = ['midProposalContent','midProposalPresentation','midDevelopmentReport','midDevelopmentPresentation','midResearchReport','midResearchPresentation','midsemGrade'];
var i=0;
for(i=0;i<RPlst.length;i++)
  document.getElementById(RPlst[i]+id).removeAttribute('disabled');
document.getElementById('edit1'+id).style.display = 'none';
document.getElementById('save1'+id).style.display = 'inline';
}

function RPedit2(id){
var RPlst = ['endDevelopmentReport','endDevelopmentPresentation','endResearchReport','endResearchPresentation','endsemGrade'];

var i=0;
for(i=0;i<RPlst.length;i++)
  document.getElementById(RPlst[i]+id).removeAttribute('disabled');
document.getElementById('edit2'+id).style.display = 'none';
document.getElementById('save2'+id).style.display = 'inline';
}
function RPsaveData1(id){
 var RPlst = ['midProposalContent','midProposalPresentation','midDevelopmentReport','midDevelopmentPresentation','midResearchReport','midResearchPresentation','midsemGrade'];

var i=0;
var x = "{";
for(i=0;i<RPlst.length;i++){
  document.getElementById(RPlst[i]+id).setAttribute('disabled',true);
  x = x+ "'"+RPlst[i]+"':'"+document.getElementById(RPlst[i]+id).value+"',";
}
x = x+"'midsemTotal':'"+document.getElementById('midsemTotal'+id).innerHTML+"'}";
  $.getJSON('/grade/RP', {x:x,type:'table1'}, function(data, jqXHR){
    if(data[0]==='OK'){
       alert('Awesome\n'+data[1]);
}else{
  alert('Error!!!!!!!!!!!!!!!!!');
}
});
  document.getElementById('save1'+id).style.display = 'none';
  document.getElementById('edit1'+id).style.display = 'inline'; 
}

function RPsaveData2(id){

 var RPlst = ['endDevelopmentReport','endDevelopmentPresentation','endResearchReport','endResearchPresentation','endsemGrade'];

var i=0;
var x = "{";
for(i=0;i<RPlst.length;i++){
  document.getElementById(RPlst[i]+id).setAttribute('disabled',true);
  x = x+ "'"+RPlst[i]+"':'"+document.getElementById(RPlst[i]+id).value+"',";
}
x = x+"'endsemTotal':'"+document.getElementById('endsemTotal'+id).innerHTML+",'Total':'"+document.getElementById('Total'+id).innerHTML+"'}";
  $.getJSON('/grade/RP', {x:x,type:'table2'}, function(data, jqXHR){
    if(data[0]==='OK'){
       alert('Awesome\n'+data[1]);
}else{
  alert('Error!!!!!!!!!!!!!!!!!');
}
});
  document.getElementById('save2'+id).style.display = 'none';
  document.getElementById('edit2'+id).style.display = 'inline'; 

}
 
 var RPx = {};
  var RPlst2 = ['endDevelopmentReport','endDevelopmentPresentation','endResearchReport','endResearchPresentation'];
  var RPlst1 = ['midProposalContent','midProposalPresentation','midDevelopmentReport','midDevelopmentPresentation','midResearchReport','midResearchPresentation'];
  RPx['endDevelopmentReport'] = 10;
  RPx['endDevelopmentPresentation'] = 5;
  RPx['endResearchReport'] = 20;
RPx['endResearchPresentation'] = 15;
  RPx['midDevelopmentReport'] = 5;
  RPx['midDevelopmentPresentation'] = 10;
  RPx['midResearchReport'] = 10;
RPx['midResearchPresentation'] = 10;
RPx['midProposalContent'] = 10;
RPx['midProposalPresentation'] = 5;
function RPabc(id){
  var z = 1;
  var midsemTotal=0;
  var endsemTotal=0;
  var i=0;
  for(i=0;i<RPlst1.length;i++){
    z = z&compare(parseInt(document.getElementById(RPlst1[i]+id).value),RPx[RPlst1[i]]);
    //alert(RPlst1[i]+z);
  if(z==0){
    alert('Incorrect Value(s)!!!');
    document.getElementById(RPlst1[i]+id).value = '0';
  return false;
  }
  midsemTotal = midsemTotal+parseInt(document.getElementById(RPlst1[i]+id).value);
}
document.getElementById('midsemTotal'+id).innerHTML = midsemTotal;
  for(i=0;i<RPlst2.length;i++){
    z = z&compare(parseInt(document.getElementById(RPlst2[i]+id).value),RPx[RPlst2[i]]);
    //alert(RPlst2[i]+z);
  if(z==0){
    alert('Incorrect Value(s)!!!');
    document.getElementById(RPlst2[i]+id).value = '0';
  return false;
  }
  endsemTotal = endsemTotal+parseInt(document.getElementById(RPlst2[i]+id).value);
}
document.getElementById('endsemTotal'+id).innerHTML = endsemTotal;
document.getElementById('Total'+id).innerHTML = midsemTotal+endsemTotal;
return true;
}


var Thesx = {};
  var Theslst1 =  ['viva1','midsemPresentation','midsemReport','viva2','finalThesis','finalViva'];
  Thesx['viva1'] = 15;
  Thesx['midsemPresentation'] = 15;
  // x['projectworkviva2'] = 15;
Thesx['midsemReport'] = 15;
  Thesx['viva2'] = 15;
   Thesx['finalThesis'] = 25;
    Thesx['finalViva'] = 15;
  
 
function Thesabc(id){
  var z = 1;
  var Total=0;
  var i=0;
  for(i=0;i<Theslst1.length;i++){
    
    z = z&compare(parseInt(document.getElementById(Theslst1[i]+id).value),Thesx[Theslst1[i]]);
    //alert(lst1[i]+z);
  if(z==0){
    alert('Incorrect Value(s)!!!'+Theslst1[i]);
    document.getElementById(Theslst1[i]+id).value = '0';
  return false;
  }
  Total = Total+parseInt(document.getElementById(Theslst1[i]+id).value);
}
document.getElementById('Total'+id).innerHTML = Total;
 return true;
}
function Thesedit(id){
  var Theslst = ['viva1','midsemPresentation','midsemReport','viva2','finalThesis','finalViva','midsemGrade','endsemGrade','seminarGrade'];
  document.getElementById('edit'+id).style.display = 'none';
  document.getElementById('save'+id).style.display = 'inline';
  var i=0;
  for(i=0;i<Theslst.length;i++){
  document.getElementById(Theslst[i]+id).removeAttribute("disabled");}
}

function ThessaveData(id){
var Theslst = ['viva1','midsemPresentation','midsemReport','viva2','finalThesis','finalViva','midsemGrade','endsemGrade','seminarGrade'];
var i=0;
var x="{";
for(i=0;i<Theslst.length;i++){
  document.getElementById(Theslst[i]+id).setAttribute("disabled", true);
  x = x+ "'"+Theslst[i]+"':"+"'"+document.getElementById(Theslst[i]+id).value+"',";
}
x=x+"'Total':'"+document.getElementById('Total'+id).innerHTML+"'}";
document.getElementById('save'+id).style.display = 'none';
  document.getElementById('edit'+id).style.display = 'inline'; 
$.getJSON('/grade/thesis', {x:x,type:'1',pk:id}, function(data, jqXHR){
    if(data[0]==='OK'){
       alert('Awesome\n'+data[1]);
}else{
  alert('Error!!!!!!!!!!!!!!!!!');
}
});
  }
 function Thesedit2(id){
  var Theslst = ['writtenAbstract','technicalContent','depthKnowledge','stylePresentation','responseQuestion'];
  document.getElementById('edit2'+id).style.display = 'none';
  document.getElementById('save2'+id).style.display = 'inline';
  var i=0;
  for(i=0;i<Theslst.length;i++){
  document.getElementById(Theslst[i]+id).removeAttribute("disabled");}
}

function ThessaveData2(idx,seminar){
  id = idx+seminar;
var Theslst = ['writtenAbstract','technicalContent','depthKnowledge','stylePresentation','responseQuestion'];
var i=0;
var x="{";
for(i=0;i<Theslst.length;i++){
  document.getElementById(Theslst[i]+id).setAttribute("disabled", true);
  x = x+ "'"+Theslst[i]+"':"+"'"+document.getElementById(Theslst[i]+id).value+"',";
}
x=x+"}";
document.getElementById('save2'+id).style.display = 'none';
  document.getElementById('edit2'+id).style.display = 'inline'; 
$.getJSON('/grade/Projects', {x:x,type:'2',pk:idx,seminar:seminar}, function(data, jqXHR){
    if(data[0]==='OK'){
       alert('Awesome\n'+data[1]);
}else{
  alert('Error!!!!!!!!!!!!!!!!!');
}
});
  }
    
 function Thesedit3(id){
  var Theslst = ['workProgress','technicalCompetence','documentation','initiative','puntuality','reliability'];
  document.getElementById('edit3'+id).style.display = 'none';
  document.getElementById('save3'+id).style.display = 'inline';
  var i=0;
  for(i=0;i<Theslst.length;i++){
  document.getElementById(Theslst[i]+id).removeAttribute("disabled");}
}

function ThessaveData3(id){
var Theslst = ['workProgress','technicalCompetence','documentation','initiative','puntuality','reliability'];
var i=0;
var x="{";
for(i=0;i<Theslst.length;i++){
  document.getElementById(Theslst[i]+id).setAttribute("disabled", true);
  x = x+ "'"+Theslst[i]+"':"+"'"+document.getElementById(Theslst[i]+id).value+"',";
}
x=x+"}";
document.getElementById('save3'+id).style.display = 'none';
  document.getElementById('edit3'+id).style.display = 'inline'; 
$.getJSON('/grade/thesis', {x:x,type:'3',pk:id}, function(data, jqXHR){
    if(data[0]==='OK'){
       alert('Awesome\n'+data[1]);
}else{
  alert('Error!!!!!!!!!!!!!!!!!');
}
});
  }

  var Disx = {};
  var Dislst1 = ['viva1','midsemPresentation','midsemReport','viva2','finalDissertation','finalViva'];
  Disx['viva1'] = 15;
  Disx['midsemPresentation'] = 15;
  Disx['midsemReport'] = 15;
Disx['viva2'] = 15;
  Disx['finalDissertation'] = 25;
  Disx['finalViva'] = 15;
  function Disabc(id){
    var z = 1;
    var Total=0;
    var i=0;
    for(i=0;i<Dislst1.length;i++){
      z = z&compare(parseInt(document.getElementById(Dislst1[i]+id).value),Disx[Dislst1[i]]);
      //alert(Dislst1[i]+z);
    if(z==0){
      alert('Incorrect Value(s)!!!');
      document.getElementById(Dislst1[i]+id).value = '0';
    return false;
    }
    Total = Total+parseInt(document.getElementById(Dislst1[i]+id).value);
  }
  document.getElementById('Total'+id).innerHTML = Total;
   return true;
  }
function Disedit(id){
  var Dislst = ['viva1','midsemPresentation','midsemReport','viva2','finalDissertation','finalViva','midsemGrade','endsemGrade'];
  document.getElementById('edit'+id).style.display = 'none';
  document.getElementById('save'+id).style.display = 'inline';
  var i=0;
  for(i=0;i<Dislst.length;i++){
  document.getElementById(Dislst[i]+id).removeAttribute("disabled");}
}

function DissaveData(id){
var  x = "{'id:'"+id+"','viva1':'"+document.getElementById('viva1'+id).value+"','midsemPresentation':'"+document.getElementById('midsemPresentation'+id).value+"','viva2':'"+document.getElementById('viva2'+id).value+"','finalDissertation':'"+document.getElementById('finalDissertation'+id).value+"','finalViva':'"+document.getElementById('finalViva'+id).value+"','Total':'"+document.getElementById('Total'+id).innerHTML+"','midsemReport':'"+document.getElementById('midsemReport'+id).value+"','midsemGrade':'"+document.getElementById('midsemGrade'+id).value+"','endsemGrade':'"+document.getElementById('endsemGrade'+id).value+"'}";
$.getJSON('/grade/dissertation', {x:x,type:'table1'}, function(data, jqXHR){
    if(data[0]==='OK'){
       alert('Awesome\n'+data[1]);
}else{
  alert('Error!!!!!!!!!!!!!!!!!');
}
});
  var Dislst = ['viva1','midsemPresentation','midsemReport','viva2','finalDissertation','finalViva','midsemGrade','endsemGrade'];
var i=0;
for(i=0;i<Dislst.length;i++)
  document.getElementById(Dislst[i]+id).setAttribute("disabled", true);
document.getElementById('save'+id).style.display = 'none';
  document.getElementById('edit'+id).style.display = 'inline';  
}
function Disedit2(id){
  var Dislst = ['workProgress','technicalCompetence','documentation','initiative','puntuality','reliability'];
var i=0;
for(i=0;i<Dislst.length;i++)
  document.getElementById(Dislst[i]+id).removeAttribute('disabled'); 
  document.getElementById('edit2'+id).style.display = 'none';
  document.getElementById('save2'+id).style.display = 'inline';
}
function DissaveData2(id){
  var Dislst = ['workProgress','technicalCompetence','documentation','initiative','puntuality','reliability'];
  var i=0;
  var x = "{";
for(i=0;i<Dislst.length;i++){
  document.getElementById(Dislst[i]+id).setAttribute('disabled',true);
  x = x+ "'"+Dislst[i]+"':"+"'"+document.getElementById(Dislst[i]+id).value+"',";
}
x=x+"}";
  $.getJSON('/grade/dissertation', {x:x,type:'table2'}, function(data, jqXHR){
    if(data[0]==='OK'){
       alert('Awesome\n'+data[1]);
}else{
  alert('Error!!!!!!!!!!!!!!!!!');
}
});
  document.getElementById('save2'+id).style.display = 'none';
  document.getElementById('edit2'+id).style.display = 'inline'; 
}

 var Prox = {};
  var Prolst1 =  ['midregularityMentor','projectViva1','projectViva2','weekdocumentSubmission','midsemViva','midsemReport']
  var Prolst2 = ['endregularityMentor','projectViva34','finalSeminar','finaldocumentSubmission'];
  Prox['midregularityMentor'] = 10;
  Prox['projectViva1'] = 5;
  Prox['projectViva2'] = 5;
Prox['weekdocumentSubmission'] = 10;
  Prox['midsemViva'] = 10;
   Prox['midsemReport'] = 10;
   Prox["endregularityMentor"] = 10
  Prox["projectViva34"] = 10
  Prox["finalSeminar"] = 15
 Prox["finaldocumentSubmission"] = 15
function Proabc(id){
  var z = 1;
  var midTotal=0;
  var total = 0;
  var i=0;
  for(i=0;i<Prolst1.length;i++){
    z = z&compare(parseInt(document.getElementById(Prolst1[i]+id).value),Prox[Prolst1[i]]);
    //alert(Prolst1[i]+z);
  if(z==0){
    alert('Incorrect Value(s)!!!'+Prolst1[i]);
    document.getElementById(Prolst1[i]+id).value = '0';
  return false;
  }
  midTotal = midTotal+parseInt(document.getElementById(Prolst1[i]+id).value);
}
document.getElementById('midsemTotal'+id).innerHTML = midTotal;
 for(i=0;i<Prolst2.length;i++){
    z = z&compare(parseInt(document.getElementById(Prolst2[i]+id).value),Prox[Prolst2[i]]);
    //alert(Prolst1[i]+z);
  if(z==0){
    alert('Incorrect Value(s)!!!'+Prolst2[i]);
    document.getElementById(Prolst2[i]+id).value = '0';
  return false;
  }
  total = total+parseInt(document.getElementById(Prolst2[i]+id).value);
}
document.getElementById('Total'+id).innerHTML = midTotal+total;
 return true;
}
function Proedit(id){
  var Prolst = ['midregularityMentor','projectViva1','projectViva2','weekdocumentSubmission','midsemViva','midsemReport','midsemGrade'];
  document.getElementById('edit'+id).style.display = 'none';
  document.getElementById('save'+id).style.display = 'inline';
  var i=0;
  for(i=0;i<Prolst.length;i++){
  document.getElementById(Prolst[i]+id).removeAttribute("disabled");}
}

function ProsaveData(id){
var Prolst = ['midregularityMentor','projectViva1','projectViva2','weekdocumentSubmission','midsemViva','midsemReport','midsemGrade'];
var i=0;
var x="{";
for(i=0;i<Prolst.length;i++){
  document.getElementById(Prolst[i]+id).setAttribute("disabled", true);
  x = x+ "'"+Prolst[i]+"':"+"'"+document.getElementById(Prolst[i]+id).value+"',";
}
x=x+"'midsemTotal':'"+document.getElementById('midsemTotal'+id).innerHTML+"'}";
document.getElementById('save'+id).style.display = 'none';
  document.getElementById('edit'+id).style.display = 'inline'; 
$.getJSON('/grade/projects', {x:x,type:'MidSem Evaluation',pk:id}, function(data, jqXHR){
    if(data[0]==='OK'){
       alert('Awesome\n'+data[1]);
}else{
  alert('Error!!!!!!!!!!!!!!!!!');
}
});
  
}
function Proedit2(id){
  var Prolst = ['endregularityMentor','projectViva34','finalSeminar','finaldocumentSubmission','endsemGrade'];
var i=0;
for(i=0;i<Prolst.length;i++)
  document.getElementById(Prolst[i]+id).removeAttribute('disabled'); 
  document.getElementById('edit2'+id).style.display = 'none';
  document.getElementById('save2'+id).style.display = 'inline';
}
function ProsaveData2(id){
  var Prolst = ['endregularityMentor','projectViva34','finalSeminar','finaldocumentSubmission','endsemGrade'];
  var i=0;
  var x = "{";
for(i=0;i<Prolst.length;i++){
  document.getElementById(Prolst[i]+id).setAttribute('disabled',true);
  x = x+ "'"+Prolst[i]+"':"+"'"+document.getElementById(Prolst[i]+id).value+"',";
}
x=x+"'Total':'"+document.getElementById('Total'+id).innerHTML+"'}";
document.getElementById('save2'+id).style.display = 'none';
  document.getElementById('edit2'+id).style.display = 'inline';
  $.getJSON('/grade/projects', {x:x,type:'EndSem Evaluation'}, function(data, jqXHR){
    if(data[0]==='OK'){
       alert('Awesome\n'+data[1]);
}else{
  alert('Error!!!!!!!!!!!!!!!!!');
}
});
   
}