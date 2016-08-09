import json


class TVMaze:
    URL = "http://api.tvmaze.com"
    searchEndpoint = "/search/shows?q=:query"
    singleSearchEndpoint = "/singlesearch/shows?q=:query"
    showEpisodes = "/shows/:id/episodes"

    @staticmethod
    def get_search_url(show_name):
        return TVMaze.URL + TVMaze.searchEndpoint.replace(":query", show_name)

    @staticmethod
    def get_single_search_url(show_name):
        return TVMaze.URL + TVMaze.singleSearchEndpoint.replace(":query",
                                                                show_name)

    @staticmethod
    def get_episodes(show_id):
        id = show_id
        if type(show_id) is int:
            id = str(show_id)
        return TVMaze.URL + TVMaze.showEpisodes.replace(":id", id)

    @staticmethod
    def get_episodes_list(json_response, season_num):
        list_of_episodes = []
        for episode in json_response:
            if episode["season"] == int(season_num):
                list_of_episodes.append(episode["name"])

        return list_of_episodes

    @staticmethod
    def get_show_id(json_response):
        return json_response[0]["show"]["id"]
