# -*- coding: utf-8 -*-

from rest_framework.views import APIView
from rest_framework import status
from rest_framework.response import Response

#Models
from games.models import (Game, Action)
from players.models import Player
from clubes.models import Club

#Util
import xml.etree.ElementTree as ET

class ImportDataView(APIView):

	def is_players_file(self, root):
		childs =  ['SORT_INFO', 'ALL_INSTANCES', 'ROWS']
		ok = True
		for child in childs:
			if not root.find(child):
				ok = False
		return ok

	def get_club(self, club_name):
		for club in self.clubes:
			if club.name == club_name:
				return club

		if not Club.objects.filter(name=club_name).exists():
			club = Club.objects.create(name=club_name, dim_x=103, dim_y=70) 
		else:
			club = Club.objects.get(name=club_name)  

		self.clubes.append(club)
		self.goals[club.name] = 0
		return club

	def get_player(self, name):
		if not Player.objects.filter(name=name).exists():
			return Player.objects.create(name=name)
		else:
			return Player.objects.get(name=name)

	def verifyGoals(self, action):
		action_goal = 'Goles'
		if action.name == action_goal:
			self.goals[action.club.name] += 1



	def importDataPlayers(self, root):
		self.clubes = []
		self.goals  = {}

		start_code    = 'Empezar marca de tiempo'
		tags          =  ['SORT_INFO', 'ALL_INSTANCES', 'ROWS']



		all_instances = root.find('ALL_INSTANCES')
		clubes  = []
		actions = []

		for instance in all_instances.findall('instance'):
			id          = instance.find('ID').text.strip()
			start       = float(instance.find('start').text.strip())
			end         = float(instance.find('end').text.strip())
			player_name = instance.find('code').text.strip()
			# print(id,start,end,player_name)
			if player_name == start_code:
				action = Action.objects.create(name=player_name, start=start, end=end)
			else:
				data_player = player_name.split('.')
				player_num  = int(data_player[0].strip())
				player_name = data_player[1].strip()
				player      = self.get_player(player_name)
				pos_x       = float(instance.find('pos_x').text.strip())
				pos_y       = float(instance.find('pos_y').text.strip())
				labels      = instance.findall('label')
				club_name   = labels[0].find('text').text.strip()
				club        = self.get_club(club_name)

				action      = labels[1].find('text').text.strip()
				description = labels[2].find('text').text.strip()


				action = Action.objects.create(
					name        = action, 
					start       = start, 
					end         = end, 
					pos_x       = pos_x,
					pos_y       = pos_y,
					player_num  = player_num,
					description = description,
					player      = player,
					club        = club,
				)
				self.verifyGoals(action)

			actions.append(action)

		local_club     = self.clubes[0]
		visiting_club  = self.clubes[1]
		local_goals    = self.goals[local_club.name]
		visiting_goals = self.goals[visiting_club.name]

		game = Game.objects.create(local_club=local_club, visiting_club=visiting_club, local_goals=local_goals, visiting_goals=visiting_goals)
		game.actions.add(*actions)
		game.save()


	def post(self,request):
		# curl -X POST http://localhost:8000/api/importer/ -F file=@/home/bcespedes/dev/tesis/aaaj/17.05.2019-gelp-aaaj-players.xml
		# import pdb; pdb.set_trace()
		if not request.FILES.get('file', False):
			return Response({'error':'XML FILE IS INVALID.'}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

		xml_file = request.FILES['file']
		tree = ET.parse(xml_file)
		root = tree.getroot()


		
		if self.is_players_file(root):
			print('Player file')
			self.importDataPlayers(root)
		else:
			print('Team file')

		return Response( status=status.HTTP_200_OK)