from src.PrettifyText import make_table, add_h_tag


class ChallengeService:
    """
    Class that provides the solution to the challenge
    """
    def exec(
        self,
        payload: dict
    ):
        """
        Method that handles the questions and adds some HTML tags to the answers
        """
        first_answer = self.solve_first_question(payload)
        second_answer = self.solve_second_question(payload)
        pretty_answers = self.make_pretty_answer(
            {
                'first_answer':first_answer,
                'second_answer':second_answer
            }
        )
        return pretty_answers

    def solve_first_question(
        self,
        payload: dict
    ):
        """
        Method which has the logic that solves the first question
        """
        legislators = payload.get('legislators')
        for legislator in legislators:
            legislator.update({
                'supported': 0,
                'opposed': 0
            })
            for vote_result in payload.get('vote_results'):
                if vote_result['legislator_id'] == legislator['id']:
                    if vote_result.get('vote_type') == '1':
                        legislator['supported'] += 1
                    else:
                        legislator['opposed'] += 1
        return legislators

    def solve_second_question(
        self,
        payload
    ):
        """
        Method which has the logic that solves the second question
        """
        bills = payload.get('bills')
        for bill in bills:
            bill.update({
                'supporters': 0,
                'opposers': 0,
                'sponsor': 'N/A'
            })
            for vote in payload.get('votes'):
                if bill.get('id') == vote.get('bill_id'):
                    bill['vote_id'] = vote.get('id')
            for legislator in payload.get('legislators'):
                if legislator.get('id') == bill.get('sponsor_id'):
                    bill['sponsor'] = legislator.get('name')
                    break
            for vote_result in payload.get('vote_results'):
                if bill['vote_id'] == vote_result['vote_id']:
                    if vote_result.get('vote_type') == '1':
                        bill['supporters'] += 1
                    else:
                        bill['opposers'] += 1
            del bill['sponsor_id']
            del bill['vote_id']
        return bills
        
    def make_pretty_answer(
        self,
        answers
    ):
        """
        Adds some HTML tags to the final answer
        """
        pretty_answer = '<!DOCTYPE html><html><body><h1>Quorum Challenge</h1>'
        first_question = '1. For every legislator available, how many bills '
        first_question += 'did the legislator support (voted for the bill)? '
        first_question += 'How many bills did the legislator oppose?'
        second_question = '2. For every bill available, how many legislators '
        second_question += 'supported the bill? How many legislators opposed '
        second_question += 'the bill? Who was the primary sponsor of the bill?'
        pretty_answer += '<style>table, th, td {border:1px solid black;}</style>'
        pretty_answer += add_h_tag(first_question)
        pretty_answer += make_table(answers['first_answer'])
        pretty_answer += add_h_tag(second_question)
        pretty_answer += make_table(answers['second_answer'])
        pretty_answer += '</body></html>'
        return pretty_answer
