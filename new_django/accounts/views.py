from django.shortcuts import render

# Create your views here.
def account(request):
    return render(request, 'accounts.html')
def register(request):
    return render(request, 'register.html')


def columnists(request, pk):
   
    writers=[
        {
            1:{
                'name':'Tolstoy',
                'title':'War and Peace',
                'publish_date':'1801',
                'about':'Tolstoy began writing War and Peace in 1863, the year that he finally married and settled down at his country estate. In September of that year, he wrote to Elizabeth Bers, his sister-in-law, asking if she could find any chronicles, diaries or records that related to the Napoleonic period in Russia. He was dismayed to find that few written records covered the domestic aspects of Russian life at that time, and tried to rectify these omissions in his early drafts of the novel.[8] The first half of the book was written and named "1805". During the writing of the second half, he read widely and acknowledged Schopenhauer as one of his main inspirations. Tolstoy wrote in a letter to Afanasy Fet that what he had written in War and Peace is also said by Schopenhauer in The World as Will and Representation. However, Tolstoy approaches "it from the other side."[9]'
            },
             
            2:{
                'name':'Duma',
                'title':'Three Musketiere',
                'publish_date':'1838',
                'about':'Dumas presents his novel as one of a series of recovered manuscripts, turning the origins of his romance into a little drama of its own. In the preface, he tells of being inspired by a scene in Mémoires de Monsieur dArtagnan (1700), a historical novel by Gatien de Courtilz de Sandras, printed by Pierre Rouge in Amsterdam, which Dumas discovered during his research for his history of Louis XIV.[1][2] According to Dumas, the incident where dArtagnan tells of his first visit to M. de Tréville, captain of the Musketeers and how, in the antechamber, he encountered three young Béarnese with the names Athos, Porthos and Aramis, made such an impression on him that he continued to investigate. That much is true – the rest is fiction: He finally found the names of the three musketeers in a manuscript titled Mémoire de M. le comte de la Fère, etc. Dumas "requested permission" to reprint the manuscript; permission was granted:'
            }    
        }
    ]
  
    writer=writers[0][pk]
    
   
    return render(request, 'authors.html',{'writer':writer})