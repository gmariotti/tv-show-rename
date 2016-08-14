class ShowFileFormat:
    format_S0xE0x = ":show - S:seasonE:epis - :name"

    @staticmethod
    def get_S0xE0x_format(episodes_list, show_name, season):
        season_num = ""
        if int(season) < 10:
            season_num += "0"
        season_num += str(season)
        list_of_files = []
        epis_num = 1
        for episode in episodes_list:
            episode_name = ShowFileFormat.format_S0xE0x.replace(":show",
                                                                show_name)
            episode_name = episode_name.replace(":season", season_num)
            epis_str = ""
            if epis_num < 10:
                epis_str = "0"
            epis_str += str(epis_num)
            episode_name = episode_name.replace(":epis", epis_str)
            episode_name = episode_name.replace(":name", episode)
            epis_num += 1
            list_of_files.append(episode_name)
        return list_of_files
