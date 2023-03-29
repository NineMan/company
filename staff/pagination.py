from rest_framework import pagination
from rest_framework.response import Response


class CustomPagination(pagination.LimitOffsetPagination):
    """Убираем поля next и previous."""

    def get_paginated_response(self, data):
        return Response({
            'count': self.count,
            # ('next', self.get_next_link()),
            # ('previous', self.get_previous_link()),
            'results': data
        })
