# -*- coding: utf-8 -*-

from rest_framework.views import APIView
from rest_framework import status
from rest_framework.response import Response

#Models
from games.models import (Player, Club)

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
		if not Club.objects.filter(name=club_name).exists():
			return Club.objects.create(name=club_name, dim_x=103, dim_y=70) 
		else:
			return Club.objects.get(name=club_name)  

	def get_player(self, name):
		pass

	def importDataPlayers(self, root):

		start_code = 'Empezar marca de tiempo'
		tags =  ['SORT_INFO', 'ALL_INSTANCES', 'ROWS']
		all_instances = root.find('ALL_INSTANCES')

		for instance in all_instances.findall('instance'):
			id          = instance.find('ID').text.strip()
			start       = instance.find('start').text.strip()
			end         = instance.find('end').text.strip()
			player_name = instance.find('code').text.strip()
			# print(id,start,end,player_name)

			if player_name != start_code:
				data_player = player_name.split('.')
				plater_num  = data_player[0].strip()
				player_name = data_player[1].strip()
				# player      = self.get_player(player_name)
				pos_x       = instance.find('pos_x').text.strip()
				pos_y       = instance.find('pos_y').text.strip()
				labels      = instance.findall('label')
				club_name   = labels[0].find('text').text.strip()
				club        = self.get_club(club_name)
				action      = labels[1].find('text').text.strip()
				description = labels[2].find('text').text.strip()
				# print(pos_x, pos_y, club_name, action, description)

			# import pdb; pdb.set_trace()


	def post(self,request):

		filename = ''
		tree = ET.parse(filename)
		root = tree.getroot()

		if self.is_players_file(root):
			self.importDataPlayers(root)
		else:
			print('Team file')

		# import pdb; pdb.set_trace()
		return Response( status=status.HTTP_200_OK)