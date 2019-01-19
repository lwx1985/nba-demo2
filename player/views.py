# Create your views here.
# Create your views here.
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.shortcuts import render
from urllib.parse import urlparse

from userControl import models


def all_player(request):
    limit_dict = {}
    limit_string = ''
    if request.method == 'GET':
        order_method = request.GET.get('order', default='-ps_g')
        string = request.GET
        list_tuple = string.items()
        for item in list_tuple:
            if item[0] != 'page' and item[0] != 'order':
                temp_key = item[0]
                if temp_key[-5:] == '_down':
                    temp_key = temp_key[0:-5] + '__gte'
                elif temp_key[-3:] == '_up':
                    temp_key = temp_key[0:-3] + '__lte'
                elif temp_key == 'player':
                    temp_key = 'player__icontains'
                limit_dict[temp_key] = item[1]
                limit_string = limit_string + '&' + item[0] + '=' + item[1]
        print(limit_string)
    else:
        order_method = '-ps_g'
        limit_string = ' '
# 分页
    contact_list = models.Season2017.objects.filter(**limit_dict).order_by(order_method)  # 获取所有contacts,假设在models.py中已定义了Contacts模型
    paginator = Paginator(contact_list, 10)  # 每页10条
    page = request.GET.get('page')

    if page is None:
        page = '1'
    t_list = paginator.page(eval(page)).object_list

    try:
        contacts = paginator.page(page)  # contacts为Page对象！
    except PageNotAnInteger:
        # If page is not an integer, deliver first page.
        contacts = paginator.page(1)
    except EmptyPage:
        # If page is out of range (e.g. 9999), deliver last page of results.
        contacts = paginator.page(paginator.num_pages)

    return render(request, 'allPlayer.html', {'contacts': contacts, 'order': order_method, 'limit_string': limit_string, 't_list': t_list})


def single_player(request):

    if request.method == 'GET':
        player_id = request.GET.get('id', default='1')
    else:
        player_id = '1'
    player_id = eval(player_id)
    player_data = models.Season2017.objects.get(id=player_id)

    if (player_data.number_2pp is None):player_data.number_2pp = 0
    else:player_data.number_2pp = round(player_data.number_2pp, 3)

    if (player_data.number_3pp is None):player_data.number_3pp = 0
    else:player_data.number_3pp = round(player_data.number_3pp, 3)

    if (player_data.fg is None):player_data.fg = 0
    else:player_data.fg = round(player_data.fg, 3)

    if (player_data.ftp is None):player_data.ftp = 0
    else :player_data.ftp = round(player_data.ftp, 3)

    avg_data = models.League.objects.get(name='avg')
    max_data = models.League.objects.get(name='max')

    player_score = {}

    player_score['2p'] = round(player_data.number_2p,3)*2
    player_score['3p'] = round(round(player_data.number_3p,3)*3,3)
    player_score['ft'] = round(player_data.ft,3)

    if player_data.ftp is None:
        player_data.ftp = 0

    if player_data.fg is None:
        player_data.fg = 0

    if player_data.number_3pp is None:
        player_data.number_3pp = 0

    return render(request, 'singlePlayer.html', {'data': player_data,'avg':avg_data,'max':max_data,'score' : player_score})


def team_data(request):
    if request.method == 'GET':
        team_id = request.GET.get('id', default='1')
    else:
        team_id = '1'

    team_id = eval(team_id)
    teams_data = models.Teams.objects.get(id=team_id)
    team_name = teams_data.name
    player_list = models.Season2017.objects.filter(tm=team_name).order_by('id')
    game_data = models.Games.objects.get(id='1')
    h_id = models.Teams.objects.get(name=game_data.home).id
    a_id = models.Teams.objects.get(name=game_data.away).id

    return render(request, 'teamData.html', {'data': teams_data, 'p_list': player_list, 'game': game_data, 'h_id': h_id, 'a_id': a_id})


def home(request):
    east_data = models.Teams.objects.filter(region='east').order_by('-win')
    west_data = models.Teams.objects.filter(region='west').order_by('-win')
    psg = models.Season2017.objects.filter().order_by('-ps_g')[0:5]
    trb = models.Season2017.objects.filter().order_by('-trb')[0:5]
    ast = models.Season2017.objects.filter().order_by('-ast')[0:5]
    blk = models.Season2017.objects.filter().order_by('-blk')[0:5]
    stl = models.Season2017.objects.filter().order_by('-stl')[0:5]
    fg = models.Season2017.objects.filter(number_2p__gte='5').order_by('-fg')[0:5]

    # for item in east_data:
    #     print(item)
    return render(request, 'home.html',{'east': east_data,'west': west_data, 'psg': psg, 'trb': trb, 'ast': ast, 'blk': blk, 'stl': stl, 'fg': fg })

def mapData(request) :
    dict_off = {'ps_g__gte': 15, 'efgp__gte': 0.5}
    off_data =  models.Season2017.objects.filter(**dict_off)
    for item in off_data :
        index = item.player.index(' ')
        item.player = item.player[index:]

    dict_trb = {'trb__gte': 8, 'orb__gte': 2}
    trb_data =  models.Season2017.objects.filter(**dict_trb)

    dict_ast = {'ast__gte': 5.5}
    ast_data =  models.Season2017.objects.filter(**dict_ast)
    for item in ast_data :
        item.orb = round(item.ast/item.tov,3)

    return render(request,'mapData.html',{'off': off_data, 'trb': trb_data, 'ast' : ast_data})

